name = 'Nicolas';
print(type(name));

# transformar el tipo de forma dinamica y de forma directa, ahora sera int
# Python infiere automaticamente el tipo de dato

name = 12;
print(type(name));

# cambio de forma dinamica

name = True;
print(type(name))

# el cambio es una parte especial de python

print('David' + ' '+ 'Darg');
print(10 + 10);

# hay que tener cuidado ahora con el tipo de datos porque no podremos hacer esto

print ('David ' + 12);

# como en este caso ambos son strings, si los podra concatenar

print ('David ' + '12');

# ahora usaremos otro ejemplo que primero marca error por la diferencia de tipos

age = 12;
print('Mi edad es ' + age);

# ahora la edad la convertimos en una cadena de texto para poderlo concatenar

age = 12;
print('Mi edad es ' + str(age));

# otra forma mas sencillo de usarlo es el formato de clases anteriores, gracias a la funcion format sabe que lo tiene que manipular como string

print(f'Mi edad es {age}')

# ahora pediremos un valor al usuario o la computadora, que originalmente esta en str, y por eso no puede recibir operaicones matematicas

age = input('Escribe tu edad => ');
print(type(age));
print(f'Tu edad en 10 años será {age}')

# para convertirlo en valor numero se utiliza el opeardor int() para que sea tratado como numero

age = input('Escribe tu edad => ');
age = int(age);
age += 10;
print(type(age));
print(f'Tu edad en 10 años será {age}')

# veremos como reacciona python al transformar un string como un nombre a un numero

age = input('Escribe tu edad => ');
age = int(age);
age += 10;
print(type(age));
print(f'Tu edad en 10 años será {age}')