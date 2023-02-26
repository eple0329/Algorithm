from itertools import combinations_with_replacement

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

for i in list(combinations_with_replacement(num_list, M)):
    for j in i:
        print(j, end = ' ')
    print()