# CRUD posibilidaid de crear, leer, actualizar y eliminar o
# Create, Read, Update & Delelte

# print
numbers = [1, 2, 3, 4, 5]

#read
print(numbers[1])

#actualizar
numbers[-1] = 10
print(numbers)

# crear y actualizar valores (agreagar al final de la lista)
numbers.append(7000)
print(numbers)

# insertar en el orden que queramos de la lista
numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'nuevo string')
print(numbers)

# unir listas
tasks =['todo 1', 'todo 2', 'todo 3']
new_list= numbers + tasks
print(new_list)

# actualizar un valor en especifico, primeor hay que saber en que posicion esta
print(new_list.index('todo 2'))
# 9

index = new_list.index('todo 2')
new_list[index] = 'todo change'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

new_numbers = [64, 0, 4, 32, 2, 16, 8 ]
new_numbers.sort()
print(new_numbers)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

#new_list.sort()
#print(new_list)
# ERROR



letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

letters.append('G')
letters[0] = 'Z'
letters.remove('C')
letters.reverse()

print(letters)