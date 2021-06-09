# setup
data = {
  "requested_gifts": []
}

greeting = """
HO HO HO!
Happy Holidays!
"""

# functions
def add_a_present():
  # get user response
  user_response = input("What would you like from Santa this year?\n(type done to exit)\n")
  # if anything but
  if user_response != 'done':
    data['requested_gifts'].append(user_response)
    add_a_present()

def ask_if_good_or_bad():
  user_response = input("Have you been good or bad this year? ")
  if user_response.lower() == 'good':
    print("\nThat's wonderful to hear!  I'm going to bring you...")
    for present in data['requested_gifts']:
      print(f'a {present}')
  elif user_response.lower() == 'bad':
    print("Oh, you've been naughty?  Expect some coal.")
  else:
    data['requested_gifts'].append('spell checker')
    print("(sigh) you mispelled a word`")
    ask_if_good_or_bad()

# print greeting
print(greeting)

# runs recursively
add_a_present()

# runs recursively
ask_if_good_or_bad()