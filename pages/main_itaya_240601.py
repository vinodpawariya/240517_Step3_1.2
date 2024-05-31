from recommend_property_itaya_240530 import recommend_property
from search_property_itaya_240530 import search_property
from auto_check_itaya_240530 import auto_check
from result_ import search_result

import streamlit as st
#from streamlit_folium import st_folium 
import folium
from streamlit_folium import folium_static

st.title("賃貸住宅検索APP")
st.snow()


#===駅データ（仮）==================================
# リストにすると表示の不具合が出たので保留。

#===初期設定で入力する値（家族形態での自動入力を後から追加する）========
#=================================================================

area_min_value = 25
area_max_value = 75

walk_min_value = 0
walk_max_value = 10

years_min_value = 10
years_max_value = 30

if "income" not in st.session_state:
    st.session_state.income = 600

if 'lifestyle' not in st.session_state:
    st.session_state.lifestyle = "エコノミー"

if "rent_min_value" not in st.session_state:
    st.session_state.rent_min_value = 5
if "rent_max_value" not in st.session_state:
    st.session_state.rent_max_value = 10

def update_rent_range():
    lifestyle = st.session_state.lifestyle
    income = st.session_state.income
    if lifestyle == "エコノミー":
        min_rent_percent = 0.15
        max_rent_percent = 0.2
    elif lifestyle == "スタンダード":
        min_rent_percent = 0.2
        max_rent_percent = 0.25
    else:  # ラグジュアリー
        min_rent_percent = 0.25
        max_rent_percent = 0.3

    temporary_min_rent = min_rent_percent * income / 12
    temporary_max_rent = max_rent_percent * income / 12

    st.session_state.rent_min_value = f"{temporary_min_rent:,.1f}"
    st.session_state.rent_max_value = f"{temporary_max_rent:,.1f}"
    return income, lifestyle, temporary_min_rent, temporary_max_rent

#===ライフスタイル情報===============================
st.sidebar.title("ライフスタイル情報の入力")
st.sidebar.write("入力情報を基に、検索条件を自動で提案します")
#===年収============================================

#スライダーで年収を選択
st.session_state.income = st.sidebar.slider("年収（万円）",
                                    value = st.session_state.income,
                                    on_change = update_rent_range,
                                    min_value = 200,
                                    max_value = 2000,
                                    step = 50)

#===家族構成========================================
col1, col2, col3 = st.columns(3)
with col1:
    number_adult = st.sidebar.number_input("大人", min_value= 1, max_value = 4,step = 1)
with col2:
    number_child = st.sidebar.number_input("小人", min_value= 0, max_value = 3, step = 1) 
with col3:
    number_baby = st.sidebar.number_input("うち未就学児", min_value= 0, max_value = number_child, step = 1)    

#===通勤地（最寄駅）=================================

commute_station =  st.sidebar.text_input("主な行先（通勤・通学）の駅名を選択")


#===物件周辺に希望する施設===========================
facility1 = st.sidebar.text_input("欲しい近隣施設1")
facility2 = st.sidebar.text_input("欲しい近隣施設2")
facility3 = st.sidebar.text_input("欲しい近隣施設3")

#===ライフスタイルの選択============================
st.session_state.lifestyle = st.sidebar.radio("希望するライフスタイル", ('エコノミー', 'スタンダード', 'ラグジュアリー'),
                                                  index=['エコノミー', 'スタンダード', 'ラグジュアリー'].index(st.session_state.lifestyle),
                                                  on_change=update_rent_range)
lifestyle=st.session_state.lifestyle

#===提案開始============================
if st.sidebar.button("提案してもらう"):
    income, lifestyle, temporary_min_rent, temporary_max_rent = update_rent_range()
    madori_recommend = auto_check(number_adult,number_child)

    df_recommend_property, df_facility_info = recommend_property(temporary_min_rent, temporary_max_rent, madori_recommend, commute_station, facility1, facility2, facility3)
    
    if facility1:
        st.write("<span style='color:red'>赤：</span>",facility1, unsafe_allow_html=True)
    if facility2:
        st.write("<span style='color:green'>緑：</span>",facility2, unsafe_allow_html=True)
    if facility3:
        st.write("<span style='color:blue'>青：</span>",facility3, unsafe_allow_html=True)
    
    # 地図の初期設定
    map_center = [35.681236, 139.767125]  # マップの中心の座標（ここでは東京タワーの座標を設定）
    mymap = folium.Map(location=map_center, zoom_start=12)


    # 施設種類ごとの色を定義
    facility_colors = {
        "facility1": 'red',
        "facility2": 'green',
        "facility3": 'blue'
    }

    # データフレームの各行に対してマーカーを追加
    for index, row in df_recommend_property.iterrows():
        #ポップアップに表示するHTMLコンテンツ
        popup_html = f"""
         <b>名称:</b> {row['名称']}<br>
         <b>アドレス:</b> {row['アドレス']}<br>
        <b>家賃:</b> {row['家賃']}万円<br>
        <b>間取り:</b> {row['間取り']}<br>
        <b>よく行く駅までの距離:</b> {row[-1]}<br>
        <div style="width: 150px; height: auto;">
            <img src="{row['間取画像URL']}" style="width: 100%; height: auto;">
        </div><br>
        <a href="{row['物件詳細URL']}" target="_blank">物件詳細</a>
        """
        popup = folium.Popup(popup_html, max_width=400)
        folium.Marker(
            location=[row['latitude'], row['longitude']],  # マーカーの座標
            popup=popup  # マーカーをクリックしたときに表示されるポップアップ
        ).add_to(mymap)

    # Streamlitに地図を表示
    folium_static(mymap)
    
    # セッション状態に保存
    st.session_state.df_recommend_property = df_recommend_property
    st.dataframe(st.session_state.df_recommend_property)

    st.session_state.df_facility_info = df_facility_info
    st.dataframe(st.session_state.df_facility_info)


#=========検索条件設定（詳細）=======================================
#==================================================================
st.sidebar.title("検索条件（詳細）")

#===希望の地域=================================

ku =  st.sidebar.multiselect("地域", options = {
    "港区",
    "目黒区",
    "千代田区",
    "世田谷区",
    "文京区",
    "中央区",
    "渋谷区",
    "豊島区",
    "江戸川区",
    "台東区",
    "足立区",
    "江東区"
})

#=========賃料設定===========
range_rent_price = st.sidebar.slider("賃料（万円）",
                  value = (float(st.session_state.rent_min_value),float(st.session_state.rent_max_value)),
                   min_value = 5.0,
                    max_value = 50.0,
                     step = 0.5 )

rent_price_min, rent_price_max = range_rent_price

rent_price_min_formatted = f"{rent_price_min:,}"
rent_price_max_formatted = f"{rent_price_max:,}"


#===管理費・共益費込み========

add_fee_included = st.sidebar.checkbox("管理費・共益費込み")

#===礼金なし========

reikin = st.sidebar.checkbox("礼金なし")

#===定期借家不可========

teiki = st.sidebar.checkbox("定期借家不可")
    
#===専有面積========

exclusive_area = st.sidebar.slider("専有面積（下限～上限）",
                  value = (area_min_value,area_max_value),
                   min_value = 15,
                    max_value = 150,
                     step = 5 )

area_min_value, area_max_value = exclusive_area

#===駅徒歩========

minutes_on_foot = st.sidebar.slider("駅徒歩（下限～上限）",
                  value = (walk_min_value,walk_max_value),
                   min_value = 0,
                    max_value = 30,
                     step = 5 )

walk_min_value, walk_max_value = minutes_on_foot

#===築年数========

years = st.sidebar.slider("築年数（下限～上限）",
                  value = (years_min_value,years_max_value),
                   min_value = 0,
                    max_value = 70,
                     step = 5 )

years_min_value, years_max_value = years

#===間取り========================================

st.sidebar.write("====================")
st.sidebar.write("間取り")
# 初期値の設定
if 'checkbox_states' not in st.session_state:
    st.session_state.checkbox_states = {
        'all_uncheck': False,
        'one_room': False,
        'one_DK_LDK': False,
        'two_DK_LDK': False,
        'three_DK_LDK': False,
        'four_DK_LDK': False
    }

# 全解除のチェックボックス
st.session_state.checkbox_states['all_uncheck'] = st.sidebar.checkbox(
    '全解除', value=st.session_state.checkbox_states['all_uncheck'])

# 全解除のチェックボックスがTrueなら、他のチェックボックスをすべてFalseに
if st.session_state.checkbox_states['all_uncheck']:
    for key in st.session_state.checkbox_states.keys():
        if key != 'all_uncheck':
            st.session_state.checkbox_states[key] = False

# 他のチェックボックス
one_room = st.sidebar.checkbox('1R / 1K', value=st.session_state.checkbox_states['one_room'])
one_DK_LDK = st.sidebar.checkbox('1DK / 1LDK', value=st.session_state.checkbox_states['one_DK_LDK'])
two_DK_LDK = st.sidebar.checkbox('2K / 2DK / 2LDK', value=st.session_state.checkbox_states['two_DK_LDK'])
three_DK_LDK = st.sidebar.checkbox('3K / 3DK / 3LDK', value=st.session_state.checkbox_states['three_DK_LDK'])
four_DK_LDK = st.sidebar.checkbox('4K / 4DK / 4LDK', value=st.session_state.checkbox_states['four_DK_LDK'])

# 他のチェックボックスのいずれかが選択された場合、全解除チェックボックスをFalseに設定
if one_room or one_DK_LDK or two_DK_LDK or three_DK_LDK or four_DK_LDK:
    st.session_state.checkbox_states['all_uncheck'] = False

madori = []
# チェックされたチェックボックスに応じた表示と状態更新
if one_room:
    st.session_state.checkbox_states['one_room'] = True
    madori.extend(['1R', '1K'])
else:
    st.session_state.checkbox_states['one_room'] = False

if one_DK_LDK:
    st.session_state.checkbox_states['one_DK_LDK'] = True
    madori.extend(['1DK', '1LDK'])
else:
    st.session_state.checkbox_states['one_DK_LDK'] = False

if two_DK_LDK:
    st.session_state.checkbox_states['two_DK_LDK'] = True
    madori.extend(['2K', '2DK', '2LDK'])
else:
    st.session_state.checkbox_states['two_DK_LDK'] = False

if three_DK_LDK:
    st.session_state.checkbox_states['three_DK_LDK'] = True
    madori.extend(['3K', '3DK', '3LDK'])
else:
    st.session_state.checkbox_states['three_DK_LDK'] = False

if four_DK_LDK:
    st.session_state.checkbox_states['four_DK_LDK'] = True
    madori.extend(['4K', '4DK', '4LDK'])
else:
    st.session_state.checkbox_states['four_DK_LDK'] = False

# 重複を除去するためにセットに変換し、再度リストに戻す
madori = list(set(madori))
# 結果を表示（デバッグ用）
print("選択された間取り:",madori)

if st.sidebar.button("検索"):
    df_search_property = search_property(ku, rent_price_min, rent_price_max, add_fee_included, reikin, teiki, area_min_value, area_max_value,walk_min_value, walk_max_value, years_min_value, years_max_value, madori)
    
    # 地図の初期設定
    map_center = [df_search_property["latitude"].mean(), df_search_property["longitude"].mean()]  # マップの中心の座標（ここでは東京タワーの座標を設定）
    mymap = folium.Map(location=map_center, zoom_start=12)

    # データフレームの各行に対してマーカーを追加
    for index, row in df_search_property.iterrows():
        #ポップアップに表示するHTMLコンテンツ
        popup_html = f"""
         <b>名称:</b> {row['名称']}<br>
         <b>アドレス:</b> {row['アドレス']}<br>
        <b>家賃:</b> {row['家賃']}万円<br>
        <b>間取り:</b> {row['間取り']}<br>
        <div style="width: 150px; height: auto;">
            <img src="{row['間取画像URL']}" style="width: 100%; height: auto;">
        </div><br>
        <a href="{row['物件詳細URL']}" target="_blank">物件詳細</a>
        """
        popup = folium.Popup(popup_html, max_width=400)
        folium.Marker(
            location=[row['latitude'], row['longitude']],  # マーカーの座標
            popup=popup  # マーカーをクリックしたときに表示されるポップアップ
        ).add_to(mymap)

    # Streamlitに地図を表示
    folium_static(mymap)

    #df_search_property["物件番号"] = range(1, len(df_search_property)+1)
    # セッション状態に保存
    st.session_state.df_search_property = df_search_property
    st.dataframe(st.session_state.df_search_property)

#search_result()

#メールで共有
st.write("余裕があったら実施")
st.button("共有する")

