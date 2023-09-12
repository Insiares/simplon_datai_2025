def fibonnaci(n):
    i=1
    itt=1
    suite=[0, 1]
    while i<n:
        i= suite[itt]+ suite[itt-1]
        suite.append(i)
        itt += 1 
        
    print(suite)

#fibonnaci(42)

def fibo2(a,b,n):
    a= a + b
    print(a)
    if a>n:
        return
    fibo2(b,a,n)

#fibo2(0,1,42)

def fibo3(n,limit):
    if n in (0,1):
        n= 1

    n = fibo3(n-1,limit) + fibo3(n-2,limit)
    if n>limit: 
        return
    print(n)

fibo3(0,42)
