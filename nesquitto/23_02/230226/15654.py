from itertools import permutations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

for i in list(permutations(num_list, M)):
    for j in i:
        print(j, end = ' ')
    print()