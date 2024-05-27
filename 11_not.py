print(not True);
# False

print(not False);
# True


# Operador logico NOT aplicado a: and
print('NOT AND');
print('NOT True and True =>', not(True and True));
# not(True and True) => False

print('NOT True and False =>', not(True and False));
# not(True and True) => True

print('NOT False and True =>', not(False and True));
# not(False and True) => True

print('NOT False and False =>', not(False and False));
# not(False and False) => True

print(not(10 > 5 and  5 < 10));
# False

print(not(10 > 5 and  5 > 10));
# True

print(not(10 < 5 and  5 < 10));
# True

print(not(10 < 5 and  5 > 10));
# True

stock = input('Ingrese el numero de stock => ');
stock = int(stock);

print(not(stock >= 10  and  stock <= 1000) )

