# ejercicio6.py

# Elabora una función que lea un caracter
# y devuelva True, si es una vocal,
# de lo contrario devuelve False
# Eje: a => True, c => False, 9 => False

def verificarVocal(caracter):
    vocales = ('a','e','i','o','u')
    existe = caracter in vocales
    print(existe)

caracter = input('Ingresar un caracter: ')
verificarVocal(caracter)