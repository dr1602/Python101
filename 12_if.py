# if se ejecuta bajo operacion booleana
if True:
    print('deberia ejecutarse');
    
# como la condicional es falsa, jamas se ejecuta
if False:
    print('nunca se ejecuta');


pet = input('Ingrese su tipo de mascota favorita: ')
respuetaAlternativa = f"No se que animal es {pet} "

if pet == 'perro' or pet == 'lobo':
    print('tienes un gusto muy perruno')
#funcion else if, que para python es elif
elif pet == 'gato' or 'leon' or 'tigre' or pet == 'lince':
    print('tienes un gusto muy felino')  
elif pet == 'pez' or 'tortuga':
    print('tus gustos son muy acuaticos')
else:
    print(respuetaAlternativa)

# funcion else, que viene acompanada del if, en caso de que no cumpla con la condicion
stock = int(input('Digita el stock => '))

if stock >= 10 and stock <= 1000:
    print(' el stock esta en niveles sanos');
else:
    print('el stock no esta en niveles sanos')

# evalua si el numero es par o impar

prompt = 'Este programa evalua si el numero de tu interes es par o impar'

print(prompt)
numero = int(input('Ingrese el numero de su interes: '))

if numero%2 == 0:
    print('Su numero es par')
elif numero%2 != 0:
    print('Su numero es impar')
else:
    print('Existe algun tipo de error, disculpe los inconvenientes.')
