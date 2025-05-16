edad = int(input('Ingresa tu edad:'))
dinero = int(input('Ingresa el monto de dinero:'))
# Validar el ingreso a la discoteca:
if(edad>=18):
    if(dinero>20):
        print("Puedes ingresar a la discoteca")
    else:
        print("No puedes ingresar")
else:
    print("No puedes ingresar, eres menor de edad")