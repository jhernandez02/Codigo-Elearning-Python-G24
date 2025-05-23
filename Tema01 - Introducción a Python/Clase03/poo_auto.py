# poo_auto.py
class Auto:
    # Atributos
    marca = ''
    modelo = ''
    placa = ''
    color = ''
    anio = ''
    combustible = 0 # Ej: 0% - 100%
    encendido = False

    def __init__(self, marca, modelo, anio, color, placa):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.placa = placa

    def getInfo(self):
        print('Combustible:',self.combustible)
    
    def encender(self):
        self.encendido = True
        print('Auto encendido')
    
    def apagar(self):
        self.encendido = False
        print('Auto apagado')

    def avanzar(self):
        if self.combustible>0 and self.encendido:
            print('Auto avanzando')
        else:
            print('Auto no tiene combustible o no esta encendido')

    def llenarTanque(self,cantidad):
        if self.combustible + cantidad > 100:
            self.combustible = 100
        else:
            self.combustible += cantidad
        print('Llenando el tanque:',cantidad)
        self.getInfo()

# Instanciamos un objeto de la clase Auto
auto1 = Auto('Yotomo','Paris', 2022, 'Pinky', 'ABC123')
auto1.getInfo()
auto1.avanzar()
auto1.encender()
auto1.avanzar()
auto1.llenarTanque(50)
auto1.avanzar()
