import streamlit as st
import sqlite3
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import re

#############
#【関数名】
#物件の提案（recommend_property）
#【処理内容】
#ひろさんご提案のロジックでDBからおすすめの物件を抽出する（件数の上限は後で決めましょう！）。
#抽出した物件それぞれについて、入力された近隣施設があるかの確認を行い、ある物件のみを残す。
#データフレームで返す。（結果表示に必要な要素は後で決めましょう。とりあえず今は全データを想定しています。）

#【パラメータ】
#・年収
#・ライフスタイル
#・家族構成（大人、子供、未就学児）
#・主な行き先の駅名
#・近隣にあってほしい施設（最大3つ）

#【返り値】
# ・おすすめ物件：データフレーム
#############

def recommend_property(temporary_min_rent, temporary_max_rent, madori_recommend, commute_station, facility1, facility2, facility3):
    # データベースに接続
    conn = sqlite3.connect('merged_DB.db')
    c = conn.cursor()

    if madori_recommend:
        placeholders = ', '.join('?' for _ in madori_recommend)

    query = """
            SELECT * FROM df_table 
            WHERE 家賃 >= ? AND 家賃 <= ?  
            AND 間取り IN ({})
            AND latitude IS NOT NULL
            """.format(placeholders)
    params = (temporary_min_rent, temporary_max_rent) + tuple(madori_recommend)
    c.execute(query, params)
    result = c.fetchall()        

    if result:
        facilities = [facility1, facility2, facility3]
        facilities = [facility for facility in facilities if facility]  # None でないものだけを残す

        if facilities:
            print(facilities)
            facility_data = []
            result_filtered = []

            for row in result:
                latitude = row[-2]  # インデックスを整数に変更（例: 4 は latitude のカラム位置）
                longitude = row[-1]  # インデックスを整数に変更（例: 5 は longitude のカラム位置）

                all_facilities_found = True
                facility_row_data = []  # このプロパティに関連する施設情報を保持するリスト

                for i, facility in enumerate(facilities):
                    # APIキー
                    API_KEY = 'AIzaSyD_0D80nd7tu68Ah7nIBjfK7vbyHPfpl9E'

                    # リクエストURL
                    URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

                    params = {
                        'location': f'{latitude},{longitude}',
                        'radius': '500',
                        'keyword': facility,
                        'key': API_KEY
                    }

                    # APIリクエストの送信
                    response = requests.get(URL, params=params)

                    # レスポンスの取得
                    data = response.json()
                    print(json.dumps(data, ensure_ascii=False))

                    if data["results"]:
                        for place in data['results']:
                            name = place['name']
                            lat = place['geometry']['location']['lat']
                            lng = place['geometry']['location']['lng']
                            # 写真のURLを取得
                            if 'photos' in place:
                                photo_reference = place['photos'][0]['photo_reference']
                                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={API_KEY}"
                            else:
                                photo_url = '写真なし'
                            
                            # このプロパティに関連する施設情報をリストに追加
                            facility_row_data.append([name, lat, lng, photo_url, f'facility{i+1}'])
                    else:
                        all_facilities_found = False
                        break

                if all_facilities_found:
                    result_filtered.append(row)
                    facility_data.extend(facility_row_data)  # 施設情報を追加

            if all_facilities_found: #入力した施設が全てあった場合
                st.write('以下の情報が見つかりました:')
                result = result_filtered
            else: #入力した施設が全くヒットしなかった場合
                st.write('該当する情報が見つかりませんでした')
                result = []
        else: #施設入力がなかった場合
            facility_data = []
            st.write('以下の情報が見つかりました:')
    else:
        st.write('該当する情報が見つかりませんでした')
        facility_data = []
    # データベース接続のクローズ
    conn.close()
    # カラム名の取得
    column_names = [description[0] for description in c.description]

    # データフレームに追加
    df_recommend_property = pd.DataFrame(result, columns=column_names) if result else pd.DataFrame(columns=column_names)
    column_names_facilities = ["名称", "緯度", "経度", "写真URL", "施設種類"]
    df_facility_info = pd.DataFrame(facility_data, columns=column_names_facilities)

    previous_station = None
    for index, row in df_recommend_property.iterrows():
        # 直前の駅名と比較
        if previous_station is not None and row["アクセス①1駅名"] == previous_station:
            # 直前の駅名と一致する場合、直前の結果を使う
            df_recommend_property.at[index, commute_station[0] + "までの時間"] = previous_result
        else:
            # 直前の駅名と一致しない場合、新しい結果を取得
            departure_station = row["アクセス①1駅名"]
            
            # 経路の取得先URL
            route_url = "https://transit.yahoo.co.jp/search/result?from="+departure_station+"&flatlon=&to="+ commute_station[0] +"&y=2024&m=05&d=30&hh=07&m0=1&m2=0"
            
            # Requestsを利用してWebページを取得する
            route_response = requests.get(route_url)
            # BeautifulSoupを利用してWebページを解析する
            route_soup = BeautifulSoup(route_response.text, 'html.parser')

            # <div class="mdSearchResult">要素を抽出
            div_element = route_soup.find('div', class_='mdSearchResult')
            section = div_element.select_one('section')
            time = section.select("span")[1]

            comments = time.find_all(string=lambda text: isinstance(text, str) and '分' in text)
            for comment in comments:
                # 正規表現を使って「分」を抽出
                match = re.search(r'\d+分', comment)
                print(match.group())
            # commute_station の値を "東京駅までの距離" 列に保存
            df_recommend_property.at[index, commute_station[0] + "までの時間"] = match.group()
            # 直前の結果を更新
            previous_station = row["アクセス①1駅名"]
            previous_result = match.group()

    return df_recommend_property, df_facility_info