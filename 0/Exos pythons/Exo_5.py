mot = str(input('Saisir un mot: '))

if len(mot)>5:
    print(f' "{mot}" contient plus de 5 caractères')
else: 
    print(f' "{mot}" fait 5 caract ou moins')