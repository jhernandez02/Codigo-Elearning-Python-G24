# Elaborar una función que tome
# como argumentos 2 numeros enteros
# y devuelva el mayor

def obtenerMayor(n1,n2):
    tupla = (n1,n2)
    return max(tupla)

print(obtenerMayor(15,10))