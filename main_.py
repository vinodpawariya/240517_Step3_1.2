from recommend_property_ import recommend_property
from search_property_ import search_property

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
area_max_value = 50

walk_min_value = 0
walk_max_value = 10

years_min_value = 10
years_max_value = 30

if "income" not in st.session_state:
    st.session_state.income = 600

if 'lifestyle' not in st.session_state:
    st.session_state.lifestyle = "エコノミー"

if "rent_min_value" not in st.session_state:
    st.session_state.rent_min_value = 50000
if "rent_max_value" not in st.session_state:
    st.session_state.rent_max_value = 100000


#===ライフスタイル情報===============================
st.sidebar.title("ライフスタイル情報の入力")
st.sidebar.write("入力情報を基に、検索条件を自動で提案します")
#===年収============================================

#スライダーで年収を選択
income = st.sidebar.slider("年収（万円）",
                                    value = st.session_state.income,
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

commute_station =  st.sidebar.multiselect("主な行先（通勤・通学）の駅名を選択", options = {
    "東京",
    "新宿",
    "池袋"
})
st.sidebar.write("詳細は後程APIを検証してから実装する（場合によっては気合と根性？）")

#===物件周辺に希望する施設===========================
facility1 = st.sidebar.text_input("欲しい近隣施設1")
facility2 = st.sidebar.text_input("欲しい近隣施設2")
facility3 = st.sidebar.text_input("欲しい近隣施設3")

#===ライフスタイルの選択============================
st.session_state.lifestyle = st.sidebar.radio("希望するライフスタイル", ('エコノミー', 'スタンダード', 'ラグジュアリー'),
                                                index=['エコノミー', 'スタンダード', 'ラグジュアリー'].index(st.session_state.lifestyle))
lifestyle=st.session_state.lifestyle

#===提案開始============================
if st.sidebar.button("提案してもらう"):
    df_recommend_property = recommend_property(income, lifestyle, number_adult, number_child, number_baby, commute_station, facility1, facility2, facility3)
    # セッション状態に保存
    st.session_state.df_recommend_property = df_recommend_property
    st.dataframe(st.session_state.df_recommend_property)
    
    # 地図の初期設定
    map_center = [35.681236, 139.767125]  # マップの中心の座標（ここでは東京タワーの座標を設定）
    mymap = folium.Map(location=map_center, zoom_start=12)

    # データフレームの各行に対してマーカーを追加
    for index, row in st.session_state.df_recommend_property.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],  # マーカーの座標
            popup=row['property name']  # マーカーをクリックしたときに表示されるポップアップ
        ).add_to(mymap)

    # Streamlitに地図を表示
    folium_static(mymap, width=1200, height=800)
    

#=========検索条件設定（詳細）=======================================
#==================================================================
st.sidebar.title("検索条件（詳細）")

#===希望駅（最寄駅）================================================

#=========賃料設定===========
range_rent_price = st.sidebar.slider("賃料（下限～上限）",
                  value = (st.session_state.rent_min_value,st.session_state.rent_max_value),
                   min_value = 50000,
                    max_value = 500000,
                     step = 5000 )

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

# チェックされたチェックボックスに応じた表示と状態更新
if one_room:
    st.session_state.checkbox_states['one_room'] = True
else:
    st.session_state.checkbox_states['one_room'] = False

if one_DK_LDK:
    st.session_state.checkbox_states['one_DK_LDK'] = True
else:
    st.session_state.checkbox_states['one_DK_LDK'] = False

if two_DK_LDK:
    st.session_state.checkbox_states['two_DK_LDK'] = True
else:
    st.session_state.checkbox_states['two_DK_LDK'] = False

if three_DK_LDK:
    st.session_state.checkbox_states['three_DK_LDK'] = True
else:
    st.session_state.checkbox_states['three_DK_LDK'] = False

if four_DK_LDK:
    st.session_state.checkbox_states['four_DK_LDK'] = True
else:
    st.session_state.checkbox_states['four_DK_LDK'] = False



if st.sidebar.button("検索"):
    df_search_property = search_property(rent_price_min, rent_price_max, add_fee_included, reikin, teiki, area_min_value, area_max_value,walk_min_value, walk_max_value, years_min_value, years_max_value, one_room, one_DK_LDK, two_DK_LDK, three_DK_LDK, four_DK_LDK)
    # セッション状態に保存
    st.session_state.df_search_property = df_search_property
    st.dataframe(st.session_state.df_search_property)
    
    # 地図の初期設定
    map_center = [35.681236, 139.767125]  # マップの中心の座標（ここでは東京タワーの座標を設定）
    mymap = folium.Map(location=map_center, zoom_start=12)

    # データフレームの各行に対してマーカーを追加
    for index, row in st.session_state.df_search_property.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],  # マーカーの座標
            popup=row['property name']  # マーカーをクリックしたときに表示されるポップアップ
        ).add_to(mymap)

    # Streamlitに地図を表示
    folium_static(mymap, width=1200, height=800)

#メールで共有
st.write("余裕があったら実施")
st.button("共有する")

# streamlit run 240516_Step3-1_example.py