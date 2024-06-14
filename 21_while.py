# while es similar al if como en

if True:
    print('Se ha ejecutado')
    
# en while seria:
# recuerda tener cuidado para que pare

'''
while True:
    print('Se ha ejecutado')
'''

counter = 0

while counter < 9:
    counter += 1
    print(f'Se ha ejecutado {counter} vez / veces')
    
    
# otra version de while con while para forzar el cierre

counter = 0

while counter < 12:
    counter += 1
    if counter == 6:
        break
    print(counter)
    
# otra version 

counter = 0

while counter < 9:
    counter += 1
    print(counter)
    if counter < 6:
        continue
    print(f'Contando hasta {counter}')