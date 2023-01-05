score = [74, 85, 69, 77, 81]
print("最高分數為", max(score))
print("最低分數為", min(score))
print("平均分數為", sum(score)/len(score))

print("升冪排序結果為", sorted(score))
print("降冪排序結果為", sorted(score, reverse=True))
# print(score.sort(reverse=True)) 為何是None

score_1 = [s for s in score if s >= 80]  # s(此處可做更新,如*2+10)為新串列元素,取出新元素到s, 條件為真的話會執行前方敘述
print("80分得以上有:", score_1)
print("80分以上的人數有:", len(score_1), "人")

city = ["東京", "名古屋", "大阪", "京都", "福岡"]
high_temp = [32, 28, 27, 26, 27]
low_temp = [25, 21, 20, 19, 22]
print("都市資料為:", city)
print("最高氣溫為:", high_temp)
print("最低氣溫為:", low_temp)
for i, j, k in zip(city, high_temp, low_temp):
    print(i, "的最高氣溫為:", j, "最低氣溫為:", k)
