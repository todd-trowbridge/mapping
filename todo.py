# import json module
import json

# json file to open
file_name = "todo.json"

# open the file todo.json and load it to the variable 'data'
with open(file_name, "r") as file_handle:
    data = json.load(file_handle)

# add todo function
def add_todo():
  # get number of todos
  count = len(data['todos'])
  # ask the user for a new todo
  todo = input("What's your todo? ")
  # add the todo
  data['todos'].append(todo)
  # save the data to a file
  with open(file_name, "w") as file_handle:
    json.dump(data, file_handle)

def print_todos():
  # keep track of count
  count = 1
  # loop through and print each todo
  for todo in data['todos']:
    print(f'{count}: {todo}')
    count += 1

while True:
  print ("""
Choose an option:
1. Print Todos
2. Add Todo
3. Remove Todo
0. Quit

Option: 
  """)

  # user input variable
  user_choice = input('')

  # read
  if user_choice == '1':
    print_todos()

  # create
  if user_choice == '2':
    add_todo()

  # delete
  if user_choice == '3':
    print_todos()
    delete_index = int(input('Which would you like to delete?'))
    del data['todos'][delete_index - 1]

  # quit
  elif user_choice == '0':
    # save the data to a file
    with open(file_name, "w") as file_handle:
      json.dump(data, file_handle)
    break