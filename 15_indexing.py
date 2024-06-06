text = 'Ella sabe Python'
print(text[0])
# E

print(text[12])
# t

#print(text[999])
# Error

print(text[10].lower())
#p

# para saber cual es el utlimo caracter y su indice

size = len(text)
print('size =>', size)
# 16
#print(text[size])
#error

print(text[size - 1])
# n

# forma optimizada de python para conocer al ultimo valor, con -1
print(text[-1])
# n

print(text[-2])
# o

# nuevo concepto: slicing (Subtexto dentro del rango)

print(text[0:6]);
# Ella s

print(text[10:16])
#Python

#si empieza desde cero, podemos obviar el primer parrafo
print(text[:10])
# Ella sabe

# sacar consulta de un punto al final
print(text[5:-1])
#sabe Pytho

# la forma correcta y sencilla es
print(text[5:])
#sabe Python

# va a ir desde el inicio hasta el final
print(text[:])
# Ella sabe Python

# en el tercer valor puedes colocar saltos que hace en el string
print(text[10:16:2])
# Pto

print(text[::3])
# Eaa tn

###  EJEMPLO PARA LA CLASE
text = 'Ella sabe Python'
print(text[:-1])
# Ella sabe Pytho

print(text[:-2])
# Ella sabe Pyth

print(text[:-3])
# Ella sabe Pyt

print(text[:-4])
# Ella sabe Py

print(text[:-5])
# Ella sabe P
