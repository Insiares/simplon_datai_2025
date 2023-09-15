'''
Écrivez une fonction qui prend un nombre entier en entrée et affiche 
la suite de Fibonacci jusqu'à l'ordre de ce nombre. La suite de Fibonacci 
est une séquence d'entiers où chaque nombre est la somme des deux nombres 
précédents. La séquence commence généralement par 0 et 1.
'''

#par ittération:
def fibonnaci(n):
    i=1
    itt=1
    suite=[0, 1]
    while itt<(n-1):
        i= suite[itt]+ suite[itt-1]
        suite.append(i)
        itt += 1 
        
    print(suite)

fibonnaci(15)

#par récursion:
def fibo3(n):
    #initialisation pour les premiers termes
    if n in range(2):
        return n
    #résultat : somme des deux termes précédents
    return fibo3(n-1) + fibo3(n-2)

#n in range(ordre)
res = [fibo3(n) for n in range(15)]
print(res)

