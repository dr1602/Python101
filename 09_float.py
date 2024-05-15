x = 3.3
print(x)
# 3.3

y = 1.1 + 2.2
print(y)
# 3.30000000000000003
# da diferente precision decimal, si se comparan no son iguales

print(x == y)
# esto es igual a false

y_string = format(y, ".2g")
# para imprimi y pero solo con 2 digitos y como string
print('str =>', y_string)

print(y_string == str(x))
# esto permite la comparacion de strings

print('*' * 10)

print(y, x)

tolerance = 0.0001
# precision decimal deseada
print(abs(x - y) < tolerance)
# forma matematica para hacer la comparacion