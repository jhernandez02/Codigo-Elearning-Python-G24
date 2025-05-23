#listas.py
cesta = ['uva','piña','kiwi','coco']

# Mostrar el contenido de la lista
print(cesta)

# Acceder a un elemento
print(cesta[2]) # kiwi

# Modificar un elemento
cesta[1] = 'melón'
print(cesta)

# Agregar un nuevo elemento
cesta.append('manzana')
print(cesta)

# Eliminar un elemento
del(cesta[3])
print(cesta)
