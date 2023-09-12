user_input = input('indiquer 5 nombres entiers, séparés par un espace')
parsed = user_input.split(' ')
res= [ ]
for x in parsed:
    res.append(int(x))
print(res)

#pour cut l'input

nb = []
for i in range(5):
   nombre = int(input('taper un nombre'))
   nb.append(nombre)
print('list: ', nb)