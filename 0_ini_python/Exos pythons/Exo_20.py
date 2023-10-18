while True:

    print('Saisir quit pour quitter')
    mot = str(input('Saisir un mot: '))

    if mot == 'quit':
        break

    if len(mot)>5:
        print(f' {mot} contient plus de 5 caractères')
    else: 
        print(f' {mot} fait 5 caract ou moins')