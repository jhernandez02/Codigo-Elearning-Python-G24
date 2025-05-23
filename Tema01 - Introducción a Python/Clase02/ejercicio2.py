# ejercicio2.py

# Desarrollar un programa que indicando el nombre de la fruta
# esta, se le elimine de la cesta
# Cada vez que se elimina, se muestra el nuevo contenido de la cestas
cesta = ['uva','piña','kiwi','coco','manzana']
fruta = input('Ingresa la fruta que deseas eliminar: ')
# Hallamos la posición de la fruta ingresada
index = cesta.index(fruta)
# Eliminamos el elemento segun el valor de index
del(cesta[index])
# Mostramos el contenido de la cesta
print(cesta)