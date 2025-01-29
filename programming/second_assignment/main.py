import time
import os
import platform

name = "Alex"
auto_mode = False

def reset_terminal() :
  system_name = platform.system()

  if system_name == "Windows" :
    os.system("cls")
  else :
    os.system("clear")


def welcome_screen() :
  global name
  print(
    "Starlight Serenade",
    "",
    f"You play as {name} (can change the name later), a young musician who returns to your hometown after years of studying abroad. One evening, while playing your guitar at the local park, you meet a mysterious girl named Luna. She’s drawn to your music, and the two of you quickly form a connection. But as you get to know her, you realize she’s hiding a secret that could change everything. Will you pursue a romance with her, or will her secret keep you apart?",
    "",
    "Note: The story is create by AI.",
    "",
    sep = "\n"
  )

  input("Press Enter to play the game...")
  
  set_name()

def set_name() :
  global name
  reset_terminal()
  time.sleep(1)
  
  print(f"Do you want to use {name} name or create your own?", "\n")
  name_confirm = input("Type \"Y\" for change the name, or Type \"N\" for use the default name: ")
  print("")

  if name_confirm.upper() == "Y" :
    name = input("Insert your name: ")
    print(f"Your name is {name}")
    time.sleep(1.5)
    set_mode()
  
  elif name_confirm.upper() == "N" :
    print(f"Your name is {name}")
    time.sleep(1.5)
    set_mode()
  
  else :
    print("Press type Y or N.")
    time.sleep(1.5)
    set_name()
  
def set_mode() :
  global auto_mode
  reset_terminal()
  time.sleep(1)
  
  print(
    "Please select normal mode or auto mode when show dialog",
    "",
    "Note: In normal mode you need to hit enter to see next dialog,",
    "but in auto mode the dialog will show every two second",
    "(this can't be change later)",
    "",
    sep = "\n"
  )

  mode_confirm = input("Type \"N\" for normal mode or type \"A\" for auto mode: ")
  print("")

  if mode_confirm.upper() == "N" :
    print("You choose normal mode.")
    time.sleep(1.5)
  
  elif mode_confirm.upper() == "A" :
    auto_mode = True
    print("You choose auto mode.")
    time.sleep(1.5)
  
  else :
    print("Press type N or A")
    time.sleep(1.5)
    set_mode()

welcome_screen()
print(name, auto_mode)