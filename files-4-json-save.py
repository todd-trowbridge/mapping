# JSON = JavaScript Object Notation
import json

superhero = {
    "name": "Wonder Woman",
    "alias": "Diana Prince",
    "gear": [
        "Lasso of Truth",
        "Bracelets of Submission"
    ],
    "vehicle": {
        "title": "Invisible Jet",
        "speed": "2000 mph",
    }
}

with open('superhero.json', 'w') as file_handler:
  json.dump(superhero, file_handler)

with open('superhero.json', 'r') as file_handler:
  # contents = file_handler.read()
  # print(contents['name'])
  data = json.load(file_handler)
  print(data['name'])