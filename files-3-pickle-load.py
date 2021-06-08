import pickle

with open('todo.pickle', 'rb') as file_handler:
  todos = pickle.load(file_handler)

  for item in todos:
    if item['completed']:
      print(f"Done: {item['title']}")
    else:
      print(f"Todo: {item['title']}")
