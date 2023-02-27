from itertools import permutations

N, M = map(int, input().split())
N_LIST = list(map(int, input().split()))

result = list(set(permutations(N_LIST, M)))
result.sort()
for i in result:
    for j in i:
        print(j, end = ' ')
    print()