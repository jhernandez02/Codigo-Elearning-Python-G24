# funciones_args.py
def promediarNotas(*args):
    print(args, type(args))
    suma = sum(args)
    total = len(args)
    return suma/total

promedioAlgoritmos = promediarNotas(11,12,18)
print('promedioAlgoritmos:', promedioAlgoritmos)
promediaBaseDatos = promediarNotas(15,16)
print('promediaBaseDatos:', promediaBaseDatos)
