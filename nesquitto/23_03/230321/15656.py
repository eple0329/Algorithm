from itertools import product

N, M = map(int, input().split())

num_list = sorted(list(map(int, input().split())))

for i in list(product(num_list, repeat=M)):
    for j in i:
        print(j, end=" ")
    print()