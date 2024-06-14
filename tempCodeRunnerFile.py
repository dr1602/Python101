person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person_social_media = {
    'twitter': '@nicobytes'
}

person.update(person_social_media)
# print(person)

person['name'] = 'Felipe'
# print(person)

del person['age']
# print(person)

print(list(person.keys()))
print(list(person.values()))