# 4.函數的練習-mersenne_prime
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
# 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。


def SieveOfEratosthenes(n, prime):
    for i in range(0, n + 1):
        prime[i] = True
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1


def mersennePrimes(n):

    prime = [0] * (n + 1)
    SieveOfEratosthenes(n, prime)
    k = 2

    while (((1 << k) - 1) <= n):
        num = (1 << k) - 1
        if (prime[num]):
            print(num, end=" ")

        k += 1

n = 10000
# n = 0
# i = 0
# for i in range(1, n+1):
#     Mp = [i]
#     if mersennePrimes(n) == True and i < 5:
#         Mp.append(n)
#         print(n)
#         i += 1
#     n += 1
# print("Mersenne prime numbers smaller",
#       "than or equal to ", n)
mersennePrimes(n)
#
#
#
#
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0 and n > 2:
#             # print(n, "不是質數")
#             return 0
#         else:
#             # print(n, "是質數")
#             return 1
#
#
# n = int(input("找出第n個質數"))
# count = 0  # 第幾個index
# num = 0  # 傳入def的值
# prime_list = list()  # 空list
# while_s = 1
# prime_list.append(2)  # 目前沒找到方法把2放入
#
# while while_s == 1:
#     ans = is_prime(num)
#
#     if ans == 1:
#         prime_list.append(num)
#         count += 1
#     else:
#         pass
#
#     if count < n:
#         num += 1
#     elif count >= n:
#         while_s = 0
#
# print(prime_list)  # 質數list
# print(prime_list[n-1])  # 找出第n個質數
#
#
#
# def is_mersenne_prime(n):
#     pl = prime_list(n)
#     m = 0
#     for j in range(1, m):
#         if pl == 2 ** m - 1:
#             print(pl, "為Mersenne Prime")
#             Imp_list.append(pl)
#             return 1
#         m += 1
#
# while_m = 1
# l_num = 0
# counts = 0
# Imp_list = list()
# while while_m == 1:
#     f_ans = is_mersenne_prime(l_num)
#
#     if ans == 1:
#         Imp_list.append(l_num)
#         counts += 1
#     else:
#         pass
#
#     if counts < n:
#         num += 1
#     elif counts >= n:
#         while_m = 0
#
#
# print(Imp_list)
