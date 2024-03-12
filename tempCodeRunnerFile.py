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
