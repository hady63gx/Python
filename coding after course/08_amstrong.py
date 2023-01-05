# 3.迴圏的練習-amstrong
# Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
#
# 說明：153=1^3+5^3+3^3，故153為Amstrong數。
#  (2^3 表示 2 的 3 次方, 3^3 表示 3 的 3 次方)

# a = 1  #9
# b = 0  #9
# c = 0  #9
# num = a * 100 + b * 10 + c
# am = a^3+b^3+c^3
# 找num = am

for num in range(100, 999):
    # num = int(input("數字"))
    a = num // 100
    b = num % 100 // 10
    c = num % 10 // 1
    # print(a, b, c)
    am = a ** 3+b ** 3+c ** 3
    # print(am)
    if num == am:
        print(num, "為Amstrong數。")
    else:
        pass


# for a in range(1, 10):
#     for b in range(0, 10):
#         for c in range(0, 10):
#             num = a * 100 + b * 10 + c
#             am = a ** 3 + b ** 3 + c ** 3
#             if num == am:
#                 print(num, "為Amstrong數。")
#             else:
#                 pass
