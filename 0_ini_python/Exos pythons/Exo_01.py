'''
___ Exo 1 ____
Écrivez un programme qui demande à l'utilisateur de 
saisir un nombre entier positif et affiche tous les 
nombres de 1 jusqu'à ce nombre (inclus).
'''

nb = int(input('Choisir un entier positif'))
for i in range(1,nb+1):  
    print(i)

# y = nb.replace(',' , '.')
# ^ un exemple pour gérer les virgules pour les floats