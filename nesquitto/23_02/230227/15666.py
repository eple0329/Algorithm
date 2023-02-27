from itertools import combinations_with_replacement

N, M = map(int, input().split())
N_LIST = list(set(map(int, input().split())))
N_LIST.sort()

for i in list(combinations_with_replacement(N_LIST, M)):
    for j in i:
        print(j, end = ' ')
    print()
