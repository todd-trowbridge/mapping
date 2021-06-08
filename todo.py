# import json module
import json

# json file to open
file_name = "todo.json"

#create empty dictionary
data = {}

# open the file todo.json and load it to the data variable
with open(file_name, "r") as file_handle:
    data = json.load(file_handle)

def add_todo():
  # get number of todos
  count = len(data)
  
  # set key to number of todos plus 1
  key = count + 1
  value = input("What's your todo? ")

  # add the task
  data[key] = value

  # save the data
  with open(file_name, "w") as file_handle:
    json.dump(data, file_handle)

# try to add a todo
add_todo()

# check if the addition worked
print(data)