
name = 'David'
last_name = 'Rangel'
age = 23
print(name)
print(last_name)

# concatenacion

full_name = name + ' ' + last_name
print(full_name)

quote = "I'm David. The Land's Protector"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2', template)

template = f"Hi, mi name is {name}, and my last name is {last_name}"
print('v3', template)

template = f"Hi, mi name is {name} {last_name} and my age is {age}"
print('v4', template)