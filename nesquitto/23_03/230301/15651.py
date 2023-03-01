from itertools import product

N, M = map(int, input().split())
for i in list(product(range(1, N+1), repeat=M)):
    for j in i:
        print(j, end = ' ')
    print()
