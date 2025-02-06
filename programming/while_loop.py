a = int(input("insert your password: "))
password = 10
while True :
  if a > password :
    print("too high")
    a = int(input("insert your password: "))
  elif a < password :
    print("too low")
    a = int(input("insert your password: "))
  elif a == password :
    print("pass")
    break