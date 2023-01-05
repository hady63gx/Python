# 4.選擇性敘述的練習 - refund
# 輸入在某商店購物應付金額與實付金額。
# 實付金額小於應付金額，則印出”金額不足”。
# 實付金額等於應付金額，則印出”不必找錢”。
# 實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
# 假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
# 說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。

est_pay = int(input("請輸入應付金額:"))
real_pay = int(input("請輸入實付金額:"))
#
# if real_pay > est_pay:
#     print("金額不足")
# elif real_pay == est_pay:
#     print("不必找錢")
# elif real_pay < est_pay:
#     a = real_pay - est_pay
#     print("應找回", a, "元")
# else:
#     print("輸入錯誤")

re_money = real_pay - est_pay
a = re_money//1000
b = (re_money % 1000)//500
c = (re_money % 500)//100
d = (re_money % 100)//50
e = (re_money % 50)//10
f = (re_money % 10)//5
g = (re_money % 5)//1

print("應找回", a, "張1000元")
print(b, "張500元")
print(c, "張100元")
print(d, "張50元")
print(e, "張10元")
print(f, "張5元")
print(g, "張1元")