# ejercicio1.py
# Hallar el promedio de 3 notas: teoría, práctica y examen final
# La nota de teoría vale el 30%
# La nota de práctica vale el 40%
# La nota del examen final vale el 30%

notaTeoria = int(input('Ingresa la nota de teoría: '))
notaPractica = int(input('Ingresa la nota de práctica: '))
notaExamenFinal = int(input('Ingresa la nota del exámen final: '))

promedio = notaTeoria*0.3 + notaPractica*0.4 + notaExamenFinal*0.3
print('Nota Final: ', promedio)