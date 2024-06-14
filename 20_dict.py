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

print(character)

character['age'] = 19;
character['height (cm)'] += 2;

print(character)
print(character.get('age'))
print(character.get('height (cm)'))

character['affiliations'].append('Pirate King')
print(character.get('affiliations'))

del character['race']
print(character)

character.pop('affiliations')
print(character)

# character.pop()
# con dicitionarios, pop requiere forzosamente la clave del elemento a eliminar

print(f'Los items son {character.items()}')
print(f'Los keys son {character.keys()}')
print(f'Los values son {character.values()}')