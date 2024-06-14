print('Hola Mundo, esto es Python.')

print('Hola, soy Python, y escribo en tu computadora.')

# Comentario entre lineas, operaciones matematicas

#print(12 + 5)
print(10 - 5 / 5)
print(2 * 10 % 5)
print(9 % 4)
#    print(8 / 2)

# Esto es un comentario
# No podemos escribir un comentario de varias lineas, pero si de la siguiente manera:

'''
    Este es un comentario
    que esta hecho en 
    varias lineas.
'''

"""
Esta
es
otra
forma
de
comentar
"""

import random as rd

print('Este es el juego de piedra, papel o tijera.');

user_option = input('Elige piedra, papel o tijera: ').lower();
game_options = ('piedra', 'papel', 'tijera');

if user_option in game_options:
    
    computer_option = rd.choice(game_options)
    
    print(f'Has escogido {user_option}')
    print(f'La computadora ha escogido {computer_option}')
    
    if user_option == computer_option:
        print('Esto es un empate, seleccionaron la misma opcion');
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera');
            print('El o la usuario ha ganado.');
        else:
            print('Papel gana a piedra');
            print('La computadora ha ganado.');
    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('Tijera gana a papel');
            print('La computadora ha ganado.');
        else:
            print('Papel gana a piedra');
            print('El o la usuario ha ganado.');
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel');
            print('El o la usuario ha ganado.');
        else:
            print('Piedra gana a tijera');
            print('La computadora ha ganado.');
    
else:
    
    print('Esa opción no es valida, escoge de nuevo (tienes 2 oportunidades más).')
    
    i = 0
    while i < 2:
        i += 1
        user_option = input('Elige piedra, papel o tijera: ').lower();
        
        if user_option in game_options:
            break
        
    if user_option in game_options:
        computer_option = rd.choice(game_options)
    
        print(f'Has escogido {user_option}')
        print(f'La computadora ha escogido {computer_option}')
        
        if user_option == computer_option:
            print('Esto es un empate, seleccionaron la misma opcion');
        elif user_option == 'piedra':
            if computer_option == 'tijera':
                print('Piedra gana a tijera');
                print('El o la usuario ha ganado.');
            else:
                print('Papel gana a piedra');
                print('La computadora ha ganado.');
        elif user_option == 'papel':
            if computer_option == 'tijera':
                print('Tijera gana a papel');
                print('La computadora ha ganado.');
            else:
                print('Papel gana a piedra');
                print('El o la usuario ha ganado.');
        elif user_option == 'tijera':
            if computer_option == 'papel':
                print('Tijera gana a papel');
                print('El o la usuario ha ganado.');
            else:
                print('Piedra gana a tijera');
                print('La computadora ha ganado.');
    else:
        print('Gracias por jugar.')