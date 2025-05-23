# ejercicio3.py

# Solicitar el nombre de la persona, y mostar su correo
tupla2 = (
            ('Juan','Pedro','Mateo'),
            ('juan@mail.com','pedro@mail.com','mateo@mail.com')
        )
nombres = tupla2[0]
correos = tupla2[1]
nombre = input('Ingresa el nombre: ')
index = nombres.index(nombre)
print('index:',index)
print('Correo:',correos[index])

