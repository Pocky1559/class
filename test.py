# While loop test

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

# if elif else test
ending_score = {
  'ending1': 10,
  'ending2': 99,
  'ending3': 1
}

if ending_score['ending3'] > 0 :
  print('you get ending 3')
elif ending_score['ending2'] > 0 :
  print('you get ending 2')
elif ending_score['ending1'] > 0 :
  print('you get ending 1')
else :
  print('error no information in ending_score variable')