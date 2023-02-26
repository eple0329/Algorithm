from math import ceil

N, M = map(int, input().split())
M_CALC = ceil((9 * M) / 10)
A = list(map(int, input().split()))

tmp = dict()
is_can = False
for i in range(N):
    if i >= M:
        tmp[A[i-M]] -= 1
    if A[i] not in tmp.keys():
        tmp[A[i]] = 1
    else:
        tmp[A[i]] += 1
    if tmp[A[i]] >= M_CALC:
        is_can = True
        break    
    

if is_can:
    print('YES')
else:
    print('NO')