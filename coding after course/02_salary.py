# 2.選擇性敘述的練習 - salary
# 輸入便利商店工讀生的工作時數，並計算其薪資。
# 60小時以內，時薪160元。
# 61~80小時，以時薪1.25倍計算。
# 81小時以上，以時薪1.5倍計算。
# 說明：薪資以累計方式計算。若工時為90小時，則薪資為60 * 160 + 20 * 160 * 1.25 + 10 * 160 * 1.5元。

salary = int(input("請輸入工讀時數:"))
a = salary * 160
b = 60 * 160 + (salary - 60) * 160 * 1.25
c = 60 * 160 + (salary - 60) * 160 * 1.25 + (salary - 80) * 160 * 1.5

if salary <= 60:
    print("薪資為:", a)
elif 60 < salary <= 80:
    print("薪資為:", b)
elif salary >= 81:
    print("薪資為:", c)
else:
    print("輸入錯誤")
