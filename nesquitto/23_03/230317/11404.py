import sys
from math import inf
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
cost_to_node = [[inf for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    cost_to_node[a][b] = min(cost_to_node[a][b], c)

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            cost_to_node[j][k] = min(cost_to_node[j][k], cost_to_node[j][i] + cost_to_node[i][k])

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            print(0, end=' ')
            continue
        if cost_to_node[i][j] == inf:
            print(0, end=' ')
        else:
            print(cost_to_node[i][j], end=' ')
    print()