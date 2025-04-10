niveles = int(input('Ingrese la cantidad de niveles de la piramide: '))
base = niveles * 2
espacios = niveles - 1
for c in range(1,base,2):
    print(' '*espacios+'*'*c)
    espacios = espacios - 1