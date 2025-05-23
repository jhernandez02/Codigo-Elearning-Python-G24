# funciones_kwargs.py

def mostrarDatos(**kwargs):
    print(kwargs,type(kwargs))

mostrarDatos(nombre='Firulais',tipo='conejo')
mostrarDatos(nombre='Chuletas',tipo='cerdo',color='pinky')