# funciones_retorno.py

billetera = 50

def cajeroAutomatico():
    print('Inserte su tarjeta')
    monto = int(input('Ingrese el monto:'))
    return monto

dinero = cajeroAutomatico()
billetera = billetera + dinero
print('billetera:',billetera)