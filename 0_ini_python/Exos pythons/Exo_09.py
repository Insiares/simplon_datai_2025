nombres = [-1, 4, 5, -6, 8, -7, -12, 13]

def paire(nb):
    res =[]
    for i in nb:
        if i%2==0:
            res.append(i)
    print(res)

paire(nombres)

