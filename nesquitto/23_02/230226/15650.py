from itertools import combinations

N, M = map(int, input().split())

for i in (list(combinations(range(1, N+1), M))):
    for j in i:
        print(j, end=' ')
    print()