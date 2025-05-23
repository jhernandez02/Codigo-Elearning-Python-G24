# ejercicio4.py

# Desarrollar un programa que nos entregue
# la cantidad de dias que un mes: Ene => 31, Feb => 28, Oct => 31
meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto')
dias = (31,28,31,30,31,30,31,31)
nombreMes = input('Ingrese el mes: ')
print('mes:',nombreMes)
index = meses.index(nombreMes )
print('index:',index)
print(nombreMes ,'tiene',dias[index],'días')
