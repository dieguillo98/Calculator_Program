def tree(x):
    base = x * 2
    espaces = x - 1
    for c in range(1,base,2):
        print(' '*espaces+'*'*c)
        espaces = espaces - 1


level = int(input('Enteer tree levels: '))

tree(level)