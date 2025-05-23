try:
    colores = ('azul','rojo')
    color = input('Color: ')
    print(colores.index(color))
except Exception as error:
    print(type(error).__name__)
    print('Ocurrió un error:', error)