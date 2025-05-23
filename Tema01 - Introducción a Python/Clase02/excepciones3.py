# excepciones3.py
try:
    a = int(input('Num1: '))
    b = int(input('Num2: '))
    division = a / b
    print('division:',division)
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except ValueError:
    print('Valores inválidos')