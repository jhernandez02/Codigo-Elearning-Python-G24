#poo.py

class Perro:
    # Atributos
    nombre = ''
    raza = ''
    color = ''
    fecha_nac = ''
    # Métodos
    def ladrar(self):
        self.saltar()
        print(self.nombre+' esta ladrando: wou wou wou')
    
    def saltar(self):
        print(self.nombre+' esta saltando')
    
    def comer(self):
        print(self.nombre+'esta comiendo su ricocan')

# Instanciando un objeto de la clase Perro
perrito1 = Perro()
perrito2 = Perro()
# Modificasmos los atributos de la clase
perrito1.nombre = 'Firulais'
perrito1.color = 'Negro cenizo'
perrito2.nombre = 'Boby'
perrito2.color = 'Marrón medio teñido claro zanahoria'
perrito2.raza = 'Pitbull'
# Accedemos a los métodos de la clase Perro
perrito1.ladrar()
perrito2.saltar()