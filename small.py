# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# # 1

# print(phonebook_dict['Elizabeth'])

# phonebook_dict['Kareem'] = '938-489-1234'

# # print(phonebook_dict['Kareem'])

# del phonebook_dict['Alice']

# # print(phonebook_dict)

# phonebook_dict['Bob'] = '968-345-2345'

# # print(phonebook_dict)

# print(phonebook_dict.values())

# 2

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# user_email = ramit['email']
# # print(user_email)

# first_user_interest = ramit['interests'][0]
# # print(first_user_interest)

# first_friend_email = ramit['friends'][0]['email']
# # print(first_friend_email)

# second_friend_second_interest = ramit['friends'][1]['interests'][1]
# # print(second_friend_second_interest)

def count_friends(dict):
  #copy incoming dictionary
  new_dict_local = dict.copy()
  #keep track of friends count
  count = 0
  #loop to count friends
  for friend in ramit['friends']:
    count += 1
  #add count to copy of dictionary
  new_dict_local['friends_count'] = count
  #return dictionary
  return new_dict_local

new_dict_global = count_friends(ramit)

print(new_dict_global)
print(ramit)