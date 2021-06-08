user_input = str(input('Please enter a word: '))

def word_counter(string):
  letter_dictionary = {}
  for letter in string:
    if letter in letter_dictionary:
      print('duplicate letter')
      letter_dictionary[letter] += 1
    else:
      print('new letter')
      letter_dictionary[letter] = 1
  print(letter_dictionary)

word_counter(user_input)