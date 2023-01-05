print("顯示1到10之間的偶數")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for i in range(2, 11, 2):
    print(i)

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
        j += 1
    i += 1
    print("\n")

i = 1
while i <= 5:
    print("*" * i)
    i += 1
