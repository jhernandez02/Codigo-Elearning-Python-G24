# Ingresar el monto de las ganacias por año
# Si el monto no supera los 10000, se paga 5% de impuesto
# Si el monto va entre 10000 y 20000, se paga 15% de impuesto
# Si el monto va entre 20001 y 35000, se paga 20% de impuesto
# Si el monto supero los 35000, se paga el 30% de impuesto
monto = int(input('monto: ')) # 36000
if monto<10000:
    print('5%')
elif monto<20000:
    print('15%')
elif monto<35000:
    print('20%')
else:
    print('30%')
