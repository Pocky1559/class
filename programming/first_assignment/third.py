print("temperature converter")
degree = float(input("insert degree: "))
degreeType = str(input("insert temperature type: "))

if degreeType ==  "c" or degreeType == "C" :
  convertDegree = (9 * degree + (32 * 5)) / 5
  print(convertDegree, "degree Fahrenheit")
elif degreeType == "f" or degreeType == "F" :
  convertDegree = (5 * (degree - 32)) // 9
  print(convertDegree, "degree Celsius")
else :
  print("error")