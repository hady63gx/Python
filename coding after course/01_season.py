# 1.選擇性敘述的練習 - season
# 輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。
# (備註︰春天是用 3、4和 5月，不是1、2和 3月)

try:
    season = int(input("請輸入月份:"))
except ValueError as err_name:
    print(err_name)
    print("輸入錯誤")
else:
    for i in range(1, 13):
        if season in range(3, 6):
            print("春")
            break
        elif season in range(6, 9):
            print("夏")
            break
        elif season in range(9, 12):
            print("秋")
            break
        elif season in range(1, 3) or season == 12:
            print("冬")
            break
        else:
            print("輸入錯誤")
            break
