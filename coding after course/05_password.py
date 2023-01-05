# 5.迴圏的練習 - password
# 出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
# 若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
# 若輸入不正確，再次出現”請輸入密碼”的提示。
# 若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。

count = 1
psw = "a12"
while count <= 3:
    print(count)
    password = input("請輸入密碼:")
    if password == psw:
        print("密碼輸入正確，歡迎使用本系統！")
        break
    else:
        count += 1
        continue
while count > 3:
    print("密碼輸入超過三次")
    break
