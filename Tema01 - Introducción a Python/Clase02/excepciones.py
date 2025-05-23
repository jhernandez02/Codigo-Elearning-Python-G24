# excepciones.py
try:
    a = int(input('Num1: '))
    b = int(input('Num2: '))
    division = a / b
    print('division:',division)
except:
    print('Upss, ocurrió un error')
finally:
    print('Finalizo de ejecutarse la operación')