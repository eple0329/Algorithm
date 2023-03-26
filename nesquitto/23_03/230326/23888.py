a, d = map(int, input().split())

q = int(input())

def gcd(tmp, b):
    if(b == 0):
        return tmp
    return gcd(b, tmp % b)

for i in range(q):
    A, l, r = map(int, input().split())
    if A == 1:
        tmp1 = r * (2 * a + (r-1) * d)//2
        tmp2 = (l-1) * (2 * a + (l-2) * d)//2
        print(tmp1-tmp2)
    elif A == 2:
        if l == r:
            print(a + (l-1) * d)
        else:
            print(gcd(a, d))
    else:
        continue
