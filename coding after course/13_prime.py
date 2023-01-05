# 3.函數的練習-prime
# 寫一函數get_prime (n)用來找出第n個質數。


def is_prime(n):
    for i in range(2, n):
        if n % i == 0 and n > 2:
            print(n, "不是質數")
            return 0
        else:
            print(n, "是質數")
            return 1


n = int(input("找出第n個質數"))
count = 0  # 第幾個index
num = 0  # 傳入def的值
prime_list = list()  # 空list
while_s = 1
prime_list.append(2)  # 目前沒找到方法把2放入

while while_s == 1:
    ans = is_prime(num)

    if ans == 1:
        prime_list.append(num)
        count += 1
    else:
        pass

    if count < n:
        num += 1
    elif count >= n:
        while_s = 0

print(prime_list)
print(prime_list[-1])
