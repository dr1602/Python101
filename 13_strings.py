text = 'Ella sabe programar en Python.'
print('JavaScript' in text);
# respuesta es false

print('Python' in text);
# respuesta es true


if 'Python' in text:
    print('Elegiste un gran lenguaje de progra.')
else:
    print('Existen otros lenguajes muy buenos pero no es Python')
# Elegiste un gran lenguaje de progra.

size = len('amor')
print(size)
# 4

size = len('amoreeeeee    s')
print(size)
# 15

size = len(text)
print(size)
# 30

# metodos
text = 'Ella sabe programar en Python.'
print(text, text.upper())
# ELLA SABE PROGRAMAR EN PYTHON.
print(text.lower())
# ella sabe programar en python.
print(text.count('a'))
# 4
print(text.swapcase())
# eLLA SABE PROGRAMAR EN pYTHON.
print(text.startswith('Ella'))
#true
print(text.endswith('Rust'))
#false
print(text.replace('a', 'i'))
# Elli sibe progrimir en Python.

text_2 = 'este es un titulo alternativo'
print(text_2)
# este es un titulo alternativo
print(text_2.capitalize())
# Este es un titulo alternativo
print(text_2.title())
# Este Es Un Titulo Alternativo
print(text_2.isdigit())
# false
print('999'.isdigit())
# true

help_modify = 'FECHA DE EXPIRACIÓN DE LA VACANTE'
print(help_modify.lower())