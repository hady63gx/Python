# 1. 迴圏的練習-factor
# 輸入一正整數，求其所有的因數。
# 說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36

n = int(input("請輸入一正整數"))
print(n, "的因數為:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end="\t")
    else:
        pass
