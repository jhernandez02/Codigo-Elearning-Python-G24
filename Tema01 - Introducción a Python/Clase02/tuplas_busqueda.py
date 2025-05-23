# tuplas_busqueda.py

colores  = ('rojo','azul','verde','negro','verde')
# index, devuelve la posición del elemento que se busca en la tupla
print(colores.index('verde')) # Output: 2
#print(colores.index('celeste')) # Output: Error elemento no definido

existe_color1 = "celeste" in colores
existe_color2 = "verde" in colores
print("Consulta color celeste:", existe_color1)
print("Consutla color verde:", existe_color2)