# 2.函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。


# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         return True
#
# n = int(input("是否為質數?"))
#
# if is_prime(n):
#     print(n, "不是質數")
# else:
#     print(n, "是質數")

n = int(input("是否為質數?"))


def is_prime(n):
    for i in range(1, n):
        if n % i == 0 and n > 2:
            print(n, "不是質數")
            return False
        else:
            print(n, "是質數")
            return True



is_prime(n)
