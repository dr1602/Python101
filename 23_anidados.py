# ciclos dentro de ciclos

matriz = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

print(matriz[0])
# [1,2,3]

print(matriz[0][1])
# 2

# es importante no repetir variables en los ciclos anidados
for i in matriz:
    print(i)
    for j in i:
        print(j)
        
# para hacer una denominacion de variables mas descriptiva, podemos hacer

for row in matriz:
    for column in row:
        print(column)