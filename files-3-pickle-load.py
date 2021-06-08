import pickle

with open('todo.pickle', 'rb') as file_handler:
  todos = pickle.load(file_handler)

print(todos)