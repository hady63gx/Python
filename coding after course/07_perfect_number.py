# 2.迴圏的練習-perfect_number
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
# 說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。


for n in range(1, 100):
    nList = []
    # print(n, "的因數為:")
    for i in range(1, n+1):
        if n % i == 0:
            # print(i, end="\t")
            nList.append(i)
        else:
            pass
    nListSum = sum(nList)
    # print(nList)
    if n == (nListSum-n):
        print(n, "為完美數")
    else:
        pass

