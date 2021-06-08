# import json module
import json

# json file to open
file_name = "todo.json"

# open the file todo.json and load it to the variable 'data'
with open(file_name, "r") as file_handle:
    data = json.load(file_handle)

def add_todo():
  # get number of todos
  count = len(data)
  # set key to number of todos plus 1
  key = count + 1
  # ask the user for a new todo
  value = input("What's your todo? ")
  # add the todo
  data[key] = value
  # save the data to a file
  with open(file_name, "w") as file_handle:
    json.dump(data, file_handle)

# try to add a todo
add_todo()

# check if adding the todo worked
print(data)