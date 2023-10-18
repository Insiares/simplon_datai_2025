def taille_mots(mots_input):
    res= []
    for x in mots_input:
        res.append(len(x))
    print(res)
    

mots = ['chien', 'arbre', 'tigre', 'iimutable', 'enter', 'ornithorinque', 'uhu']
taille_mots(mots)