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

def search_property(ent_price_min, rent_price_max, add_fee_included, reikin, teiki, area_min_value, area_max_value,walk_min_value, walk_max_value, years_min_value, years_max_value, one_room, one_DK_LDK, two_DK_LDK, three_DK_LDK, four_DK_LDK):
    #if add_fee_included: #合算した値で賃料を検索するロジックを組み込む
    
    #if reikin: #礼金が0もしくは、値がないもののみを抽出する
    
    #if teiki: #定期借家に該当するものを取り除く

    # 空のデータフレームを定義するための列名
    columns = ["property no.","property name","Category","Address","Nearest Station 1","Nearest Station 2","Nearest Station 3","Station Distance 1","Station Distance 2","Station Distance 3","Age of Building","Structure",
                "Number of Floors","Rent","Management Fee","Security Deposit","Key Money","Layout","Floor Area","Exterior Image <URL>","Floor Plan Image <URL>",
                "Details <URL>","Latitude","Longitude","Fixed-term Lease"]

    # 空のデータフレームを作成
    df_search_property = pd.DataFrame(columns=columns)

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
    df_search_property = pd.DataFrame(sample_data, columns=columns)

    return df_search_property
