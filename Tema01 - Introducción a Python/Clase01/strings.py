mensaje = 'Mi nuevo mensaje'
print(mensaje)
print('Primer caracter:',mensaje[0])
total = len(mensaje)
print('Total caracteres:', total)
print('Último caracter:', mensaje[total-1])

mensaje = "Python es chevere"
print('Total caracteres:', len(mensaje))
# [start_index:stop_index:step]
print('mensaje[3:13:2]',mensaje[3:13:2])

texto = "Mi nuevo Mensaje"
print(texto)
print(texto.upper()) # convierte a mayúscula
print(texto.lower()) # convierte a minúscula
# convierte mayus a minus y minus a mayus
print(texto.swapcase())
# convierte todo a minus y a mayus solo la primera letra
print(texto.capitalize())
