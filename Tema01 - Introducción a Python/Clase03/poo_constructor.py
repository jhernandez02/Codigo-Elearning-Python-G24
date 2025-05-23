# poo_constructor.py
class Mascota:
    # Atributos
    nombre = ''
    especie = ''

    # Definimos el constructor de la clase
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

    def getNombre(self):
        print('Nombre: '+self.nombre)
    
    def getEspecie(self):
        print('Especie: '+self.especie)

mascota1 = Mascota('Firulais','Perro')
mascota1.getNombre()
mascota1.getEspecie()

mascota2 = Mascota('Bigotes','Gato')
mascota2.getNombre()
mascota2.getEspecie()