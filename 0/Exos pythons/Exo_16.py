n=42
while True:
    x=int(input('Rentrer le nombre à deviner'))
    if x>42:
        print('Plus petit!')
    elif x<42: 
        print('plus grand!')
    else:
        print('GG!')
        break