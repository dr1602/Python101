numbers = [1, 2, 3, 4]
print(numbers)
# [1, 2, 3, 4]
print(type(numbers))
# <class 'list'>

tasks = ['make the dishes', 'play games']
print(tasks)
# ['make the dishes', 'play games']

types = [1, True, 'hola']
print(types)
# [1, True, 'hola']

print(numbers[0])
# 1

print(tasks[0])
# make the dishes

text = 'Hola'
print(type(text))
# string

# text[0] = 'W'
# ERROR, strings no permiten esas mutaciones

tasks[0] = 'watch platzi courses'
print(tasks)
# ['watch platzi courses', 'play games']

tasks[0] = 'do the dishes'
print(tasks)
# ['do the dishes', 'play games']

print(numbers[:3])
# [1, 2, 3]
# deja afuera al valor en el indice 3 y toma del indice 0 al 2

print(True in types)
# True

print('hola' in types)
# True