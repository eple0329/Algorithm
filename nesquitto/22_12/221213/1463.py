N = int(input())

dimention = 1000000

def Three(n, dim):
    global dimention
    if dim >= dimention:
        return
    
    n //= 3
    dim += 1

    if n == 1:
        dimention = dim
        return
    else:
        if n % 3 == 0:
            Three(n, dim)
        if n % 2 == 0:
            Two(n, dim)
        One(n, dim)
        
def Two(n, dim):
    global dimention
    if dim >= dimention:
        return
    
    n //= 2
    dim += 1

    if n == 1:
        dimention = dim
        return
    else:
        if n % 3 == 0:
            Three(n, dim)
        if n % 2 == 0:
            Two(n, dim)
        One(n, dim)

def One(n, dim):
    global dimention
    if dim >= dimention:
        return
    
    n -= 1
    dim += 1

    if n == 1:
        dimention = dim
        return
    else:
        if n % 3 == 0:
            Three(n, dim)
        if n % 2 == 0:
            Two(n, dim)
        One(n, dim)

if N == 1:
    print(0)
else:
    if N % 3 == 0:
        Three(N, 0)
    if N % 2 == 0:
        Two(N, 0)
    One(N, 0)

    print(dimention)

