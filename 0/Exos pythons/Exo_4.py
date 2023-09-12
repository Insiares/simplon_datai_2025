def signe(n):
    if type(n)!= int:
        print('indiquer un entier')
        raise TypeError
    if n>0:
        print(f' {n} est positif')
    elif n<0:
        print(f' {n} est négatif')
    else:
        print(f' {n} est nul')

signe('e')