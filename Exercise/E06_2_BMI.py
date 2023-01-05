condition = 1
while condition == "1":
    h = float(input("請輸入身高(cm):"))
    w = float(input("請輸入體重(kg):"))
    bmi = w / (h/100) ** 2

    print("您的身高為:", h, "(cm)", "體重為:", w, "(kg)")
    print("BMI值為:", bmi)

    if bmi < 18.5:
        print("*****體重過瘦*****")
    elif 18.5 <= bmi < 24:
        print("*****體重標準*****")
    elif 24 <= bmi < 27:
        print("*****體重過重*****")
    elif 27 <= bmi < 30:
        print("*****輕度肥胖*****")
    elif 30 <= bmi < 35:
        print("*****中度肥胖*****")
    elif bmi >= 35:
        print("*****重度肥胖*****")
    else:
        print("請檢查以上數值")

    while True:
        condition = input("請輸入代碼(1.繼續2.停止")
        if condition == "1" or condition == "2":
            break
        else:
            print("輸入錯誤請重新輸入")
