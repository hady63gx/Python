num1 = [99, 98, 97, 87, 78, 56, 87, 87]
print("score資料:", num1)

del_n = int(input("請輸入要刪掉的值:"))

while del_n in num1:
   num1.remove(del_n)
print("刪除後的score資料:", num1)
