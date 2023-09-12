voyels = ['a', 'i' ,'e' ,'o' ,'u']
mots = ['chien', 'arbre', 'tigre', 'iimutable', 'enter', 'ornithorinque', 'uhu']


def tri_mot(mots_input):
    idx = []
    res = []
    for x in mots_input:
        if x[0] in voyels:
            idx.append(mots_input.index(x))
    for y in idx:
        res.append(mots_input[y])
    print(res)

tri_mot(mots)

# en une ligne : [y for y in l if y[0] in "aeuoiy"]


