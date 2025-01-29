import time
import os
import platform

game_name = "Starlight Serenade"
name = "Pocky"

def reset_terminal() :
  system_name = platform.system()

  if system_name == "Windows" :
    os.system("cls")
  else :
    os.system("clear")

def welcome_screen() :
  global name
  global game_name
  
  print(
    game_name,
    "",
    f"You play as {name} (can change the name later), a young musician who returns to your hometown after years of studying abroad. One evening, while playing your guitar at the local park, you meet a mysterious girl named Luna. She’s drawn to your music, and the two of you quickly form a connection. But as you get to know her, you realize she’s hiding a secret that could change everything. Will you pursue a romance with her, or will her secret keep you apart?",
    "",
    "Note: The story is create by AI.",
    "",
    sep = "\n"
  )

  input("Press Enter to set the name in game...")
  
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
    print(f"Your name is {name}", "\n")
    input("Please Enter to play game...")
  
  elif name_confirm.upper() == "N" :
    print(f"Your name is {name}", "\n")
    input("Please Enter to play game...")
  
  else :
    print("Press type Y or N.")
    time.sleep(1.5)
    set_name()

def delay(text) :
  return len(text) / 20

def show_dialog(array) :
  for text in array :
    print(text)
    time.sleep(delay(text))

def show_option(array) :
  for text in array :
    print(text)

welcome_screen()

reset_terminal()
time.sleep(1)
print(game_name)
time.sleep(3.5)
reset_terminal()
time.sleep(1.5)

# Chapter 1
show_dialog([
  "Chapter 1: The Melody in the Park",
  "",
  "The sun is setting, casting a golden glow over the park.",
  "You sit on a bench, strumming your guitar, lost in thought.",
  "The melody you play is soft and melancholic, reflecting your feelings of being back in a place filled with memories.",
  "",
  "As you finish the song, you hear a soft clap.",
  "You look up and see a girl with silver hair and piercing blue eyes standing a few feet away.",
  "She smiles shyly.",
  "",
  "Luna: \"That was beautiful. What’s the name of the song?\"",
  f"{name}: \"Oh, it’s... something I’m still working on. I’m {name}, by the way.\"",
  "Luna: \"I’m Luna. Do you play here often?\"",
  "",
  "You notice something strange about her—her presence feels almost otherworldly, but you can’t quite put your finger on it.",
  "",
])

show_option([
  "1. \"Not really. I just came back to town and needed some fresh air.\"",
  "2. \"I used to, a long time ago. It feels good to be back.\"",
  "3. \"Only when the stars are out. It feels like the right time to play.\""
])

def option1() :
  chapter = input("Choose your response: ")

  print("")
  if chapter == "1" :
    show_dialog([
      "Luna tilts her head, her silver hair catching the moonlight.",
      "Luna: \"Fresh air is good for the soul. Maybe the park brought us both here tonight.\"",
      "She sits beside you, and the two of you talk about your lives.",
      "You feel an instant connection, as if you’ve known her for years."
    ])

  elif chapter == "2" :
    show_dialog([
      "Luna’s eyes light up.",
      "Luna: \"So you’re a hometown hero, huh? I’ve always loved this park. It feels... magical.\"",
      "She sits beside you, and you share stories about your childhood.",
      "You notice she avoids talking about her own past, but her laughter is infectious."
    ])

  elif chapter == "3" :
    show_dialog([
      "Luna’s lips curve into a mysterious smile.",
      "Luna: \"The stars do have a way of bringing people together, don’t they?\"",
      "She sits beside you, and the two of you gaze at the night sky.",
      "You feel a strange sense of peace, as if the universe itself is watching over you."
    ])

  else :
    print("Please put the number 0-2")
    time.sleep(2)
    option1()

option1()