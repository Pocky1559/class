password = int(input('insert password: '))

while password != 10 :
  print('your password is not correct')

  if password > 10 :
    print('your number is higher than the password')
    password = int(input('please try again: '))
  else :
    print('your number is lesser than the password')
    password = int(input('please try again: '))

print('correct')