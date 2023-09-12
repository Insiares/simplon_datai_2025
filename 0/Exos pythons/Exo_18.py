nombres = [-1, 4, -6, 8, -12]

def positifs(nb):
    res = []
    i=0
    while i <= len(nb)-1 :
        if nb[i]>0:
            res.append(nb[i])
            i+= 1
            
        else:
            i += 1 
        
    print(res)
        
        
        

positifs(nombres)