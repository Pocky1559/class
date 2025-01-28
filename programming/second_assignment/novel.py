import time
import sys

need_info = {
  "current_route_id": "a1",
  "name": None
}

print(need_info)

print(
  "Welcome to my visual novel game!",
  "This is an assignment from my teacher.",
  "The code in this game I just make for fun only.",
  "Anyway thank you so much for playing my game!",
  "Note: If you see \"...\" you need to hit enter to open the next dialog.",
  sep= "\n"
)
input("Click Enter to play...")

class novel :
  def __init__(self):
    self.matching_route = None

    for route in routes :
      if need_info["current_route_id"] == route["id"] :
        self.matching_route = route
        break
      
      print("Error access the database")
      print(f"{need_info["current_route_id"]} does not exist")
      sys.exit()
  
  def show_dialog(self) :
    for text in self.matching_route["dialogs"] :
      print(text)
      time.sleep(1)
    self.show_input()
  
  def show_input(self) :
    info = self.matching_route["inputs"]

    if info["type"] == "text" :
      need_info[info["variable_name"]] = input(info["text"])
      need_info["current_route_id"] = info["next_route_id"]
      self.__init__()

    

routes = {
  "id": "a1",
  "dialogs": [
    "Oh, Hi!",
    "Welcome to my world!",
    "What is your name?"
  ],
  "inputs": {
    "type": "text",
    "variable_name": "name",
    "text": "Insert your name: ",
    "next_route_id": "a2"
  }
}, {
  "id": "a2",
  "dialogs": [
    f"{need_info["name"]}?",
    "That is a really nice name!",
    "Anyway my name is Meow",
    "Also nice to meet you!"
  ],
  "input": {
    "Type": "choice",
    "number_of_choice": 1,
    "choice": [{
      "text": "Nice to meet you too!",
      "next_route_id": "a3"
    }]
  }
}

display = novel()

display.show_dialog()