sale = {"東京": 80, "名古屋": 60, "京都": 22, "大阪": 150, "福岡": 75}
print("現在資料為:", sale)
k = input("請輸入要新增的鍵值:")
if k in sale:
    print("已經有", k, "這筆資料了")
else:
    d = input("請輸入要新增的資料:")
    sale[k] = d
    print("新增了", k, "的資料", d)
print("現在資料為:", sale)

t = input("要更改哪個鍵值的資料?")
if t in sale:
    print(t, "的資料為", sale[t])
    d = int(input("請輸入要變更的資料:"))
    sale[t] = d
    print(t, "的資料被變更為:", sale[t])
else:
    print("找不到", t, "這筆資料")
print("現在資料為:", sale)

c = input("要刪除哪個鍵值資料?")
if c in sale:
    print(c, "的資料為", sale[c])
    del sale[c]
    print("資料被刪除了")
else:
    print("找不到", c, "這筆資料")
print("現在資料為:", sale)
