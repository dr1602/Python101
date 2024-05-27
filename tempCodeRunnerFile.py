prompt = 'Este programa evalua si el numero de tu interes es par o impar'

print(prompt)
numero = int(input('Ingrese el numero de su interes: '))

if numero%2 == 0:
    print('Su numero es par')
elif numero%2 != 0:
    print('Su numero es impar')
else:
    print('Existe algun tipo de error, disculpe los inconvenientes.')
