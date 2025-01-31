# While loop

a = int(input())
i= 1
while i < a :
  print((str(i)) * i)
  i += 1

number = int(input('Enter a number: '))
while number != 0 :
  print('your number is', number)
  number = int(input('Enter a number: '))
print('The end.')

x = int(input())
while True :
  if x == 10 :
    print('***10***')
    break
  elif x > 10 :
    print(x)
    x -= 1
  elif x < 10 :
    print(x)
    x += 1