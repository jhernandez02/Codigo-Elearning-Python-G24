#ejercicio2b.py

cesta = ['uva','piña','kiwi','coco','manzana']
fruta = input('Ingresa la fruta que deseas eliminar: ')
existe = fruta in cesta

if existe:
    index = cesta.index(fruta)
    del(cesta[index])
    print(cesta)
else:
    print('La fruta no encuentra en la cesta')