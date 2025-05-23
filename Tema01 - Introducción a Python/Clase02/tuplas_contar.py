# tuplas_contar.py

notas = (9,11,16,18,20,13,10,15,16,9,19,13,9,13)
total = len(notas)
print('Total de notas:',total)

# Hallamos cuantas veces se repita la nota 13
print('Cantidad de 13s:', notas.count(13))

# Hallamos la nota máxima
maxima_nota = max(notas)
print('Nota máxima:', maxima_nota)

# Hallamos la nota mínimos
minima_nota = min(notas)
print('Nota mínima:', minima_nota)

# Hallamos cuantas veces se repita la nota mínima
print('Cantidad con la nota mínima:', notas.count(minima_nota))

# Hallamos el promedio de notas
suma_nota = sum(notas)
promedio_nota = suma_nota / total
print('Promedio Notas:', promedio_nota)

