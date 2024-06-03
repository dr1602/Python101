import random as rd

user_option = input('Elige piedra, papel o tijera: ');
game_options = ['piedra', 'papel', 'tijera'];

computer_option = rd.choice(game_options)

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