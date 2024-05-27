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
import pandas as pd

def recommend_property(income,lifestyle,number_adult,number_child,number_baby,commute_station,facility1,facility2,facility3):
    #ライフスタイルに合わせた係数の設定
    if lifestyle == "エコノミー":
        min_rent_percent = 0.15
        max_rent_percent = 0.2
    elif lifestyle == "スタンダード":
        min_rent_percent = 0.2
        max_rent_percent = 0.25
    else:  # ラグジュアリー
        min_rent_percent = 0.25
        max_rent_percent = 0.3

    rent_min_value = int(min_rent_percent * income * 10000 / 12)
    rent_max_value = int(max_rent_percent * income * 10000 / 12)

    # 空のデータフレームを定義するための列名
    columns = ["property no.","property name","Category","Address","Nearest Station 1","Nearest Station 2","Nearest Station 3","Station Distance 1","Station Distance 2","Station Distance 3","Age of Building","Structure",
                "Number of Floors","Rent","Management Fee","Security Deposit","Key Money","Layout","Floor Area","Exterior Image <URL>","Floor Plan Image <URL>",
                "Details <URL>","Latitude","Longitude","Fixed-term Lease"]

    # 空のデータフレームを作成
    df_recommend_property = pd.DataFrame(columns=columns)

    # 追加するサンプルデータ
    sample_data = [
        [1,"ノースプリムラ","賃貸アパート","東京都あきる野市伊奈","JR Itsukaichi Line/Musashi Masuko Station","JR Itsukaichi Line/Musashi Hikida Station","-",5,24,"-",10,"2-story","1st floor",65000,2800,"-",65000,"1LDK","44.18㎡","-","-","-",35.5378631,139.5951104,"可"],
        [2,"サンハイツナカヅカ","賃貸マンション","東京都あきる野市秋川３","JR Itsukaichi Line/Akigawa Station","JR Itsukaichi Line/Musashi Hikida Station","JR Itsukaichi Line/Higashi-Akiru Station",10,22,38,35,"4-story","2nd floor",57000,2000,"-","-","3LDK","53.51㎡","-","-","-",35.56,139.6,"不可"],
        [3,"サンハイツナカヅカ","賃貸マンション","東京都あきる野市秋川３","JR Itsukaichi Line/Akigawa Station","JR Itsukaichi Line/Musashi Hikida Station","JR Itsukaichi Line/Higashi-Akiru Station",10,22,38,35,"4-story","2nd floor",57000,2000,"-","-","3LDK","53.51㎡","-","-","-",35.56,139.6,"不可"],
        [4,"サンハイツナカヅカ","賃貸マンション","東京都あきる野市秋川３","JR Itsukaichi Line/Akigawa Station","JR Itsukaichi Line/Musashi Hikida Station","JR Itsukaichi Line/Higashi-Akiru Station",10,22,38,35,"4-story","2nd floor",57000,2000,"-","-","3LDK","53.51㎡","-","-","-",35.56,139.6,"不可"],
        [5,"サンハイツナカヅカ","賃貸マンション","東京都あきる野市秋川３","JR Itsukaichi Line/Akigawa Station","JR Itsukaichi Line/Musashi Hikida Station","JR Itsukaichi Line/Higashi-Akiru Station",10,22,38,35,"4-story","2nd floor",57000,2000,"-","-","3LDK","53.51㎡","-","-","-",35.56,139.6,"不可"],
        [6,"サンハイツナカヅカ","賃貸マンション","東京都あきる野市秋川３","JR Itsukaichi Line/Akigawa Station","JR Itsukaichi Line/Musashi Hikida Station","JR Itsukaichi Line/Higashi-Akiru Station",10,22,38,35,"4-story","2nd floor",57000,2000,"-","-","3LDK","53.51㎡","-","-","-",35.56,139.6,"不可"],
        [7,"サンハイツナカヅカ","賃貸マンション","東京都あきる野市秋川３","JR Itsukaichi Line/Akigawa Station","JR Itsukaichi Line/Musashi Hikida Station","JR Itsukaichi Line/Higashi-Akiru Station",10,22,38,35,"4-story","2nd floor",57000,2000,"-","-","3LDK","53.51㎡","-","-","-",35.56,139.6,"不可"],
        [8,"サンハイツナカヅカ","賃貸マンション","東京都あきる野市秋川３","JR Itsukaichi Line/Akigawa Station","JR Itsukaichi Line/Musashi Hikida Station","JR Itsukaichi Line/Higashi-Akiru Station",10,22,38,35,"4-story","2nd floor",57000,2000,"-","-","3LDK","53.51㎡","-","-","-",35.56,139.6,"不可"],
    ]

    # サンプルデータをデータフレームに追加
    df_recommend_property = pd.DataFrame(sample_data, columns=columns)

    return df_recommend_property
