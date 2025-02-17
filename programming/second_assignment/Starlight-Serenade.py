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
    time.sleep(1)

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
        time.sleep(2.5)
        continue


    elif name_confirm.upper() == "N" :
      print(f"Your name is {name}", "\n")
      input("Please Enter to play game...")
      break

    else :
      print("Press type Y or N.")
      time.sleep(1.5)

def delay(text) :
  return len(text) / 20

def show_dialog(array) :
  for text in array :
    print(text)
    time.sleep(delay(text))

def show_option(array) :
  for text in array :
    print(text)

# run the game
reset_terminal()
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
      "Luna: \"The stars do have a way of bringing people togetheStarlight Serenader, don’t they?\"",
      "She sits beside you, and the two of you gaze at the night sky.",
      "You feel a strange sense of peace, as if the universe itself is watching over you."
    ])
    break

  else :
    print("Please put the number 1-3")
    time.sleep(2)

input('\nPlease enter to go to the next chapter')
reset_terminal()

# Chapter 2
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
    ending_score["ending1"] += 1
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
    time.sleep(2)

input('\nPlease enter to go to the next chapter')
reset_terminal()

# Chapter 3
show_dialog([
  'Chapter 3: The Secret Revealed',
  '',
  'Over the next few days, you and Luna grow closer.',
  'She starts showing up at the park every evening, and you find yourself looking forward to seeing her.',
  'But one night, something strange happens.',
  '',
  'As you play a new song for her, the air around you seems to shimmer.',
  'Luna’s eyes glow faintly, and for a moment, you see a pair of translucent wings behind her.',
  '',
  f'{name}: "Luna... what are you?"',
  f'Luna: (hesitates) "I... I’m not human, {name}. I’m a star spirit. I came to Earth to experience life, but my time here is limited."',
  '',
  'You’re stunned.',
  'Luna looks at you with a mix of fear and hope, waiting for your reaction.',
  '',
  'What do you say?',
  ''
])

show_option([
  '1. "It doesn’t matter what you are. I care about you, Luna."',
  '2. "How long do you have left here?"',
  '3. "This is too much. I need some time to think."'
])

while True :
  chapter = input('Choose your response: ')

  print('')
  if chapter == '1' :
    ending_score["ending1"] += 1
    show_dialog([
      'Luna’s eyes fill with tears, and she smiles.',
      'Luna: "You really mean that, don’t you?"',
      'She takes your hand, and you feel a warm, glowing energy pass between you.'
    ])
    break
  
  elif chapter == '2' :
    ending_score["ending1"] += 1
    show_dialog([
      'Luna looks down, her voice barely a whisper.',
      'Luna: "One month. That’s all I have left."',
      'The weight of her words hangs in the air, and you feel a pang of sadness.'
    ])
    break
  
  elif chapter == '3' :
    ending_score['ending3'] += 1
    show_dialog([
      'Luna nods, her expression resigned.',
      'Luna: "I understand. Take all the time you need."',
      'She stands and walks away, leaving you alone in the park.'
    ])
    break

  else :
    print("Please put the number 1-3")
    time.sleep(2)

input('\nPlease enter to go to the next chapter')
reset_terminal()

# Chapter 4
show_dialog([
'Chapter 4: Choices and Consequences',
''
])

if ending_score['ending3'] > 0 :
  show_dialog([
    'After learning Luna’s secret, you struggle to process what it means.',
    'You distance yourself, unsure of how to handle the truth.',
    'Luna, sensing your hesitation, stops coming to the park.',
    '',
    'Days turn into weeks, and you realize you haven’t seen her since that night.',
    'You return to the park, hoping to find her, but she’s nowhere to be found.',
    'The stars above seem dimmer, as if a part of their light has vanished.',
    '',
    f'{name}: "Luna... I’m sorry."',
    '',
    'You never see her again, and the memory of her becomes a haunting reminder of what could have been.',
    'The story ends with you sitting alone in the park, strumming your guitar under the empty night sky.',
    '',
    'You got Lost Connection ending\n(Tragic Ending)'
  ])

elif ending_score['ending2'] > 0 :
  show_dialog([
    'You and Luna spend her final month together, creating beautiful memories.', 
    'You take her to your favorite places, play music for her, and share your dreams.',
    'But as the days pass, the inevitability of her departure looms over you.',
    '',
    'On her last night, the two of you sit under the stars.',
    'Luna takes your hand and smiles, though her eyes are filled with tears.',
    '',
    f'Luna: "Thank you for making my time here so special. I’ll never forget you, {name}."',
    '',
    'As the first light of dawn breaks, Luna’s form begins to fade.',
    'She disappears, leaving behind only the memory of her laughter and the warmth of her touch.',
    'Though heartbroken, you know you gave her the best of your world, and her time with you was a gift.',
    '',
    'You got Fleeting Moments ending\n(Bittersweet Ending)'
])

elif ending_score['ending1'] > 0 :
  show_dialog([
    'After learning Luna’s secret, you vow to make the most of your time together.',
    'As the days pass, you grow even closer, and Luna begins to hope that maybe, just maybe, she can stay on Earth with you.',
    '',
    'On the final night of her time on Earth, you play a song for her under the stars.',
    'As the last note fades, Luna’s form begins to shimmer.',
    'But instead of disappearing, she transforms into a human, her star spirit essence merging with the Earth.',
    '',
    f'Luna: "You gave me a reason to stay, {name}. The stars may have brought me here, but you made me want to remain."',
    '',
    'The two of you embrace, knowing that your love has transcended the boundaries between worlds.',
    '',
    'You got Eternal Starlight ending\n(Romantic Ending)'
  ])

else :
  print('system unable to access variable ending_score')

print(
  '',
  '',
  'That all for my game!',
  'Thank you so much for playing this game.',
  'My name is Pocky (web developer) and this game is for school assignment.',
  'I know it beyond the work that teacher told me to do, but I love codind and I have so much fun creating this game!',
  '',
  'Anyway if you found bug or have question you can contact me at <pocky1559@proton.me>',
  'or Discord <pocky_aviation>',
  sep='\n')