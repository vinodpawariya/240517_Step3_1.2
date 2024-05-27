import streamlit as st
import pandas as pd

def search_result():
    # ファイル読み込み
    try:
        df = pd.read_csv("240521_DB_test.csv", encoding="utf-8")
    except UnicodeDecodeError:
    # 文字化けが発生した場合の処理
        result = chardet.detect(df.head(1).to_string().encode("utf-8"))
        detected_encoding = result["encoding"]
        df = pd.read_csv("DB.csv", encoding=detected_encoding)


    st.dataframe(data = df, height = 200)

    st.write("=======================")

