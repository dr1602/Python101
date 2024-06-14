my_dict = {}

print(type(my_dict))
print(my_dict)

my_dict = {
    'name': 'Mario Alberto',
    'last_name': 'Lee Brown',
    'age': 34  
}

print(my_dict)
print(len(my_dict))

print(my_dict['name'])
print(my_dict['age'])
# print(my_dict['profesion'])
# error

print(my_dict.get('last_name'))
print(my_dict.get('profesion'))
# none

print('profesion' in my_dict)
# false
print('age' in my_dict)
# true