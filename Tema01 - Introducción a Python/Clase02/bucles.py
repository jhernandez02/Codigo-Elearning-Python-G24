print('--- Bucle Range ---')
print(range(8))

for i in range(8):
    print(i)

print('--- Bloque range ---')
for i in range(2,8):
    print(i)

print('--- Desde una lista ---')
cesta = ['azul','rojo','verde','negro']
for color in cesta:
    print(color)

print('--- Bucle while ---')
condicion = True
cont = 0
while condicion:
    numero = int(input('Ingresa un número: '))
    cont += 1
    if numero>100:
        condicion = False
        print('cont:',cont)
