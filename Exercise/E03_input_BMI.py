h = float(input("請輸入身高(cm):"))
w = float(input("請輸入體重(kg):"))
bmi = w / (h/100) ** 2

print("您的身高為:", h, "(cm)\t體重為:", w, "(kg)")
print("BMI值為:", bmi)
