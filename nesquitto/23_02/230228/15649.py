from itertools import permutations

N, M = map(int, input().split())
a = list(permutations(range(1, N+1), M))
for i in a:
    for j in i:
        print(j, end=' ')
    print()