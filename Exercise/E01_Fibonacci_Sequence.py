# 1 1 2 3 5 8 13 21 34 55 89

def fun(i):
   if i > 1:
      return fun(i-1) +fun(i-2)
   return 1






data = int(input("請問要做到費式數列第幾項?"))
for i in range(data):
   print(fun(i), end=",")
