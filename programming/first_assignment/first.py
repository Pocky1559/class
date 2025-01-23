print("grade calculator")
score = int(input("insert points: "))
if score < 50 :
    print("F")
elif score >= 50 and score < 55 :
    print("D")
elif score >= 55 and score < 60 :
    print("D+")
elif score >= 60 and score < 65 :
    print("C")
elif score >= 65 and score < 70 :
    print("C+")
elif score >= 70 and score < 75 :
    print("B")
elif score >= 75 and score < 80 :
    print("B+")
elif score >= 80 and score <= 100 :
    print("A")
else :
    print("error")