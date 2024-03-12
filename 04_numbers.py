lives = 3
print(type(lives))
print(lives)
age = 12
budget = 120000

impots = 1.16
temperature = 23.192

print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)
print(type(lives))

lives = lives / 2
print(type(lives))

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number = 700000000000000000000.12
print(number)

number_small = 0.0000000000000000000000002
print(number_small)

## Es una buena practica que con solo leer sepamos de que trata la variable, como las vidas

## Programa que calcule el promedio del gasto de 3 meses (Enero, Febrero, Marzo, y uno con promedio)

## Simple
enero = 3000
febrero = 4000
marzo = 5000
presupuest_promedio = (enero + febrero + marzo)/ 3

template = "El presupuesto promedio de 3 meses es: {}".format(presupuest_promedio)

print(template)

## Intermediate
print("¿Cuánto gastaste en enero?")
month_01 = int(input())
print("¿Cuánto gastaste en febrero?")
month_02 = int(input())
print("¿Cuánto gastaste en marzo?")
month_03 = int(input())
presupuest_promedio = (month_01 + month_02 + month_03)/ 3

template = "El presupuesto promedio de 3 meses es: {}".format(presupuest_promedio)

print(template)

## More then Intermediate
def my_budget(month_one, month_two, month_three):
    presupuest_promedio = (month_one + month_two + month_three)/ 3
    template = "El presupuesto promedio de 3 meses es: {}".format(presupuest_promedio)
    print(template)
    
my_budget(3000, 4000, 5000)


