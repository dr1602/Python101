# ya tienen un numero de condiciones dadas

for element in range(9):
    print(element);
    
# para iniciar desde un punto definido

for element in range(1, 10):
    print(element);
    
# sirve para recorrer estructuras o listas, o diccionarios o tuplas

my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print(element)

my_tuple = ( 'piedra', 'papel', 'tijeras')

for element in my_tuple:
    print(element)
    
character = {
    'name': 'Monkey',
    'last_name': 'D. Luffy',
    'pseudonym': ['Mugiwara', 'Fifth Emperor', 'Joy Boy' ],
    'race': 'human',
    'affiliations': [
        'Dadan Family (formerly)',
        'Straw Hat Pirates',
        'Straw Hat Grand Fleet', 
        'Ninja-Pirate-Mink-Samurai Alliance (dissolved)',
        'The Four Emperors'
    ],
    'bounties': {
        'First (Belly)': 30000000,
        'Second (Belly)': 100000000,
        'Third (Belly)': 300000000,
        'Fourth (Belly)': 400000000,
        'Fifth (Belly)': 500000000,
        'Sixth (Belly)': 1500000000,
        'Current (Belly)': 3000000000,
    },
    'age': 17,
    'height (cm)': 172
}

'''
for element in character:
    print(element)
    
for element in character['affiliations']:
    print(element)
    
for i in character:
    print(f'key => {character[i]}')
'''
    
for key, value in character.items():
    print(f'{key} => {value}')
    
nakamas = [
    {
        'name': 'Monkey D. Luffy',
        'position': 'Captian',    
    },
    {
        'name': 'Nami',
        'position': 'Navigator',    
    },
    {
        'name': 'Roronoa Zoro',
        'position': '1st Commander',    
    },

]
    
for i in nakamas:
    print('name of nakama: ', i['name'])
    
# Playgrounds:

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇

for i in my_list:
    if i > 0:
        new_list.append(i)

print(new_list)