#poo_metodos.py
class Robot:
    nombre=''
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self, nombre):
        print('Hola '+nombre+', me llamo '+self.nombre)

robot1 = Robot('Bee')
robot1.saludar('Jhonathan')