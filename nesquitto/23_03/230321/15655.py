from itertools import combinations

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

a = combinations(num_list, M)
for i in a:
    for j in i:
        print(j, end=" ")
    print()