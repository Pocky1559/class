print("BMI calculator")
weight = float(input("weight: "))
height = float(input("insert height: "))
bmi = weight / (height ** 2)

print(f"your BMI is: {bmi}")
if bmi < 18.50 :
    print("you are too thin")
elif bmi >= 18.50 and bmi < 25.00 :
    print("you are normal")
elif bmi >= 25.00 and bmi < 30.00 :
    print("you should eat less")
elif bmi >= 30.00 and bmi < 35.00 :
    print("you should go on diet")
else :
    print("you should go and see a doctor")