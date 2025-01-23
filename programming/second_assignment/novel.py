import time

def show_dialog(array) :
  for text in array :
    print(text)
    time.sleep(1)

show_dialog([
  'Hi',
  'My name is Meow',
  'Nice to meet you'
])