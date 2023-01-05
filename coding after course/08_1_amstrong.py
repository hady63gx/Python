# 3.迴圏的練習-amstrong
# Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
#
# 說明：153=1^3+5^3+3^3，故153為Amstrong數。
#  (2^3 表示 2 的 3 次方, 3^3 表示 3 的 3 次方)

num = input()
ans = []
for i in num:
    # print(i)
    ans.append(int(i))
# print(ans)
if num == (ans[0] ** 3 + ans[1] ** 3 + ans[2] ** 3):
    print(num, "為Amstrong數。")
else:
    print("Nooooooooooooo")


# aaa = 0
# num = input()
# ans = []
# for i in num:
#     # print(i)
#     ans.append(int(i))
# # print(ans)
# aaa == ans[0] ** 3 + ans[1] ** 3 + ans[2] ** 3
# if num = ans:
#     print(num, "為Amstrong數。")
# else:
#     pass
