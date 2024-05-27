import streamlit as st
import sqlite3

#############
#【関数名】
#物件の検索（search_property）
#【処理内容】
#入力された条件と一致する物件をDB上から抽出する（件数の上限は後で決めましょう！）。
#データフレームで返す。（結果表示に必要な要素は後で決めましょう。とりあえず今は全データを想定しています。）

#【パラメータ】
#・賃料（下限～上限）
#・管理費共益費込みか
#・礼金有無
#・定期借家不可か
#・専有面積（下限～上限）
#・駅徒歩（下限～上限）
#・築年数（下限～上限）
#・間取り

#【返り値】
# ・おすすめ物件：データフレーム
#############
import pandas as pd

def search_property(rent_price_min, rent_price_max, add_fee_included, reikin, teiki, area_min_value, area_max_value,walk_min_value, walk_max_value, years_min_value, years_max_value, madori):
    # データベースに接続
    conn = sqlite3.connect('merged_DB.db')
    c = conn.cursor()

    if madori:
        placeholders = ', '.join('?' for _ in madori)    

    if add_fee_included and reikin: #管理費込みで礼金0のものの場合
        # 条件をもとにデータベースクエリの実行
        query = """
        SELECT * FROM df_table 
        WHERE 家賃 >= ? AND 家賃 <= ? 
        AND (礼金 = 0 OR 礼金 = '') 
        AND 面積 >= ? AND 面積 <= ? 
        AND 築年数 >= ? AND 築年数 <= ? 
        AND `アクセス①1徒歩(分)` >= ? AND `アクセス①1徒歩(分)` <= ? 
        AND 間取り IN ({})
        AND latitude IS NOT NULL
        """.format(placeholders)
        params = (rent_price_min, rent_price_max, area_min_value, area_max_value, years_min_value, years_max_value, walk_min_value, walk_max_value) + tuple(madori)
        c.execute(query, params)
        result = c.fetchall()        
        # 一致するデータの表示
        if result:
            st.write('以下の情報が見つかりました:')
            #for row in result:
        else:
            st.write('該当する情報が見つかりませんでした')

    elif add_fee_included: #管理費込みの場合
        # 条件をもとにデータベースクエリの実行
        query = """
        SELECT * FROM df_table 
        WHERE 家賃 >= ? AND 家賃 <= ? 
        AND (礼金 = 0 OR 礼金 = '') 
        AND 面積 >= ? AND 面積 <= ? 
        AND 築年数 >= ? AND 築年数 <= ? 
        AND `アクセス①1徒歩(分)` >= ? AND `アクセス①1徒歩(分)` <= ?  
        AND 間取り IN ({})
        AND latitude IS NOT NULL
        """.format(placeholders)
        params = (rent_price_min, rent_price_max, area_min_value, area_max_value, years_min_value, years_max_value, walk_min_value, walk_max_value) + tuple(madori)
        c.execute(query, params)
        result = c.fetchall()
        
        # 一致するデータの表示
        if result:
            st.write('以下の情報が見つかりました:')
        else:
            st.write('該当する情報が見つかりませんでした')

    elif reikin: #礼金0のものの場合
        # 条件をもとにデータベースクエリの実行
        query = """
        SELECT * FROM df_table 
        WHERE 家賃 >= ? AND 家賃 <= ? 
        AND (礼金 = 0 OR 礼金 = '') 
        AND 面積 >= ? AND 面積 <= ? 
        AND 築年数 >= ? AND 築年数 <= ? 
        AND `アクセス①1徒歩(分)` >= ? AND `アクセス①1徒歩(分)` <= ?  
        AND 間取り IN ({})
        AND latitude IS NOT NULL
        """.format(placeholders)
        params = (rent_price_min, rent_price_max, area_min_value, area_max_value, years_min_value, years_max_value, walk_min_value, walk_max_value) + tuple(madori)
        c.execute(query, params)
        result = c.fetchall()        
        # 一致するデータの表示
        if result:
            st.write('以下の情報が見つかりました:')
        else:
            st.write('該当する情報が見つかりませんでした')

    else: #家賃のみ
        # 条件をもとにデータベースクエリの実行
        query = """
        SELECT * FROM df_table 
        WHERE 家賃 >= ? AND 家賃 <= ? 
        AND (礼金 = 0 OR 礼金 = '') 
        AND 面積 >= ? AND 面積 <= ? 
        AND 築年数 >= ? AND 築年数 <= ? 
        AND `アクセス①1徒歩(分)` >= ? AND `アクセス①1徒歩(分)` <= ? 
        AND 間取り IN ({})
        AND latitude IS NOT NULL
        """.format(placeholders)
        params = (rent_price_min, rent_price_max, area_min_value, area_max_value, years_min_value, years_max_value, walk_min_value, walk_max_value) + tuple(madori)
        c.execute(query, params)
        result = c.fetchall()
        
        # 一致するデータの表示
        if result:
            st.write('以下の情報が見つかりました:')
        else:
            st.write('該当する情報が見つかりませんでした')

    # データベース接続のクローズ
    conn.close()

    #if add_fee_included: #合算した値で賃料を検索するロジックを組み込む
    
    #if reikin: #礼金が0もしくは、値がないもののみを抽出する
    
    #if teiki: #定期借家に該当するものを取り除く


    # 空のデータフレームを定義するための列名
    # カラム名の取得
    column_names = [description[0] for description in c.description]

    # データフレームに追加
    df_search_property = pd.DataFrame(result, columns=column_names)
    return df_search_property
