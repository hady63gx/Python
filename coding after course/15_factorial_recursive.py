# 5.遞迴函數的練習-factorial_recursive
# 寫一遞迴函數factorial (n)用來計算1*2*3*…*n的值。
# 提示：factorial (n) = n * factorial(n-1)，factorial(1)=1


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("請輸入要計算的階層"))
print(factorial(n))

