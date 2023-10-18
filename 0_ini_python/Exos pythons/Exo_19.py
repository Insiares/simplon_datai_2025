voyels = ['a', 'i' ,'e' ,'o' ,'u']
mots = ['chien', 'arbre', 'tigre', 'iimutable', 'enter', 'ornithorinque', 'uhu']


def tri_mot(mots_input):
    i = 0
    res = []
    while i <= len(mots_input)-1:
        mot=mots_input[i]
        if mot[0] in voyels:
            res.append(mots_input[i])
            i += 1
        else:
            i+=1
    print(res)

tri_mot(mots)