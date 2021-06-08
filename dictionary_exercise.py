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
  user_response = input("What would you like from Santa this year or if you can't think of anymore type 'done'\n")
  if user_response != 'done':
    data['requested_gifts'].append(user_response)
    print(data)
    add_a_present()

def ask_if_good_or_bad():
  user_response = input("Have you been good or bad this year?\n")
  if user_response.lower() == 'good':
    for present in data['requested_gifts']:
      print("That's wonderful to hear!  I'm going to bring you...")
      print(f'a {present}')
  elif user_response.lower() == 'bad':
    print("Oh, you've been naughty?  Expect some coal.")
  else:
    data['requested_gifts'].append('an electronic spell checker')
    print("(sigh) I've added an electronic spell checker to your list of gifts.")

# print greeting
print(greeting)

# run recursive add presents
add_a_present()

# list presents or coal
ask_if_good_or_bad()
