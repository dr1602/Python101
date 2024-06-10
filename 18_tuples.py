numbers = ( 1, 2, 3, 4)
strings = ( 'inicio', 'medio', 'medio', 'final')
print(numbers)
# acceder a un elemento de la tupla
print('0 => ', numbers[0])
print('0 => ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# prueba de CRUD
# numbers.append(10)
# print(numbers)
# no funcionan porque son solo de lectura

# numbers[1] = 'change'
# marca error tambien

# metodos de tupla

print(strings)
print(strings.index('medio'))

# cuantas veces hay un elemento en la tupla
print(strings.count('medio'))
# frecuencai de: 2

# si se pueden hacer transformaciones, entre tuplas y listas
my_list = list(strings)

print(type(my_list))
print(my_list)

# y este cambio a lista, o lista, si la podemos modificar
my_list[1] = 'segundo acto'
print(my_list)

# podemos modificar de lista a tupla
my_tuple = tuple(my_list)

print(type(my_tuple))
print(my_tuple)