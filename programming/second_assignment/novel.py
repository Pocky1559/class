# import all importan file
import time
import os
import platform

# set all of the necessary variable
game_name = "Starlight Serenade"
name = "Pocky"
ending_score = {
  'ending1': 0,
  'ending2': 0,
  'ending3': 0
}

# set all of the necessary function
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
  while True :
    reset_terminal()
    # time.sleep(1)

    print(f"Do you want to use {name} name or create your own?", "\n")
    name_confirm = input("Type \"Y\" for change the name, or Type \"N\" for use the default name: ")
    print("")

    if name_confirm.upper() == "Y" :
      insert_name = input("Insert your name: ")

      if insert_name != '' :
        name = insert_name
        print(f"Your name is {name}", "\n")
        input("Please Enter to play game...")
        break
      else :
        print('\nName cannot be empty please put your name again.')
        # time.sleep(2.5)
        continue


    elif name_confirm.upper() == "N" :
      print(f"Your name is {name}", "\n")
      input("Please Enter to play game...")
      break

    else :
      print("Press type Y or N.")
      # time.sleep(1.5)

def delay(text) :
  return len(text) / 20

def show_dialog(array) :
  for text in array :
    print(text)
    # time.sleep(delay(text))

def show_option(array) :
  for text in array :
    print(text)

# run the game
reset_terminal()
welcome_screen()

reset_terminal()
# time.sleep(1)
print(game_name)
# time.sleep(3.5)
reset_terminal()
# time.sleep(1.5)

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
  'What do you say?',
  ''
])

show_option([
  "1. \"Not really. I just came back to town and needed some fresh air.\"",
  "2. \"I used to, a long time ago. It feels good to be back.\"",
  "3. \"Only when the stars are out. It feels like the right time to play.\""
])

while True :
  chapter = input("Choose your response: ")

  print("")
  if chapter == "1" :
    show_dialog([
      "Luna tilts her head, her silver hair catching the moonlight.",
      "Luna: \"Fresh air is good for the soul. Maybe the park brought us both here tonight.\"",
      "She sits beside you, and the two of you talk about your lives.",
      "You feel an instant connection, as if you’ve known her for years."
    ])
    break

  elif chapter == "2" :
    show_dialog([
      "Luna’s eyes light up.",
      "Luna: \"So you’re a hometown hero, huh? I’ve always loved this park. It feels... magical.\"",
      "She sits beside you, and you share stories about your childhood.",
      "You notice she avoids talking about her own past, but her laughter is infectious."
    ])
    break

  elif chapter == "3" :
    show_dialog([
      "Luna’s lips curve into a mysterious smile.",
      "Luna: \"The stars do have a way of bringing people together, don’t they?\"",
      "She sits beside you, and the two of you gaze at the night sky.",
      "You feel a strange sense of peace, as if the universe itself is watching over you."
    ])
    break

  else :
    print("Please put the number 1-3")
    # time.sleep(2)

input('\nPlease enter to go to the next chapter')
reset_terminal()

show_dialog([
  'Chapter 2: A Glimpse of Mystery',
  '',
  'Luna sits beside you, and the two of you talk for hours.',
  'She’s curious about your music, and you find yourself opening up to her in a way you haven’t with anyone else.',
  '',
  'As the night deepens, Luna glances at the sky.',
  '',
  f'Luna: "The stars are so bright tonight. Do you believe in fate, {name}?"',
  f'{name}: "I’m not sure. Why do you ask?"',
  'Luna: "Sometimes, I feel like the stars guide us to where we’re meant to be."',
  '',
  'You notice her shiver slightly, though the night isn’t cold.',
  '',
  'What do you do?',
  ''
])

show_option([
  '1. Offer her your jacket.',
  '2. Ask if she’s okay.',
  '3. Joke, "Are you saying the stars brought us together?"'
])

while True :
  chapter = input('Choose your response: ')

  print('')
  if chapter == '1' :
    ending_score["ending1"] += 1
    show_dialog([
      'You take off your jacket and drape it over her shoulders.',
      'Luna looks surprised but grateful.',
      'Luna: "Thank you... You’re very kind."',
      'Her voice is soft, and for a moment, you see a faint glow in her eyes.'
    ])
    break
  
  elif chapter == '2' :
    ending_score["ending2"] += 1
    show_dialog([
      'You lean closer, concern in your voice.',
      f'{name}: "Are you okay? You seem... distant."',
      'Luna hesitates, then smiles.',
      'Luna: "I’m fine. Just... lost in thought."',
      'Her smile doesn’t quite reach her eyes, and you sense she’s hiding something.'
    ])
    break
  
  elif chapter == '3' :
    ending_score["ending2"] += 1
    show_dialog([
      'You grin and nudge her playfully.',
      f'{name}: "Are you saying the stars brought us together?"',
      'Luna laughs, a sound like wind chimes in the breeze.',
      'Luna: "Maybe they did. Or maybe it’s just luck."',
      'Her laughter fades, and she looks at you with a hint of sadness.'
    ])
    break

  else :
    print("Please put the number 1-3")
    # time.sleep(2)