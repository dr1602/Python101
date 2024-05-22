# Operador logico: and
print('AND');
print('True and True =>', True and True);
# True and True => True

print('True and False =>', True and False);
# True and True => False

print('False and True =>', False and True);
# False and True => False

print('False and False =>', False and False);
# False and False => False

print(10 > 5 and  5 < 10);
# True

print(10 > 5 and  5 > 10);
# False

print(10 < 5 and  5 < 10);
# False

print(10 < 5 and  5 > 10);
# False

stock = input('Ingrese el numero de stock => ');
stock = int(stock);

print(stock >= 10  and  stock <= 1000 )

# Operador logico: or
print('OR');
print('True or True =>', True or True);
# True and True => True

print('True or False =>', True or False);
# True and True => True

print('False or True =>', False or True);
# False and True => True

print('False or False =>', False or False);
# False and False => False

role = input('Digita el rol => ');
print('Estatus de acceso', role == 'admin' or role == 'vendedor');
