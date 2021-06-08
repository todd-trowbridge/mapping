import pickle

to_do_list = [
  {
    "title": "Sand the floor",
    "priority": 1,
    "completed": True
  },
  {
    "title": "Wax on, wax off",
    "priority": 2,
    "completed": False
  },
  {
    "title": "Paint the fence",
    "priority": 3,
    "completed": False
  }
]

with open('todo.pickle', 'wb') as file_handler:
  pickle.dump(to_do_list, file_handler)