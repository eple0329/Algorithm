import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

RELATION_LIST = []
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    RELATION_LIST.append((A-1, B-1))

min_cabin_bacon = [[100 for i in range(N)] for j in range(N)]
sum_cabin_bacon = []

for i in range(N):
    queue = deque()
    is_visited = [i]
    
    for j in RELATION_LIST:
        if j[0] == i:
            queue.append(j[1])
            min_cabin_bacon[i][j[1]] = 1
            min_cabin_bacon[j[1]][i] = 1
        elif j[1] == i:
            queue.append(j[0])
            min_cabin_bacon[i][j[0]] = 1
            min_cabin_bacon[j[0]][i] = 1

    while queue:
        tmp = queue.popleft()
        if tmp not in is_visited:
            is_visited.append(tmp)
            for j in RELATION_LIST:
                if j[0] == tmp and j[1] not in is_visited:
                    queue.append(j[1])
                    min_cabin_bacon[i][j[1]] = min(min_cabin_bacon[i][j[1]], min_cabin_bacon[i][tmp] + 1)
                    min_cabin_bacon[j[1]][i] = min_cabin_bacon[i][j[1]]
                elif j[1] == tmp and j[0] not in is_visited:
                    queue.append(j[0])
                    min_cabin_bacon[i][j[0]] = min(min_cabin_bacon[i][j[0]], min_cabin_bacon[i][tmp] + 1)
                    min_cabin_bacon[j[0]][i] = min_cabin_bacon[i][j[0]]
for i in min_cabin_bacon:
    sum_cabin_bacon.append(sum(i))
print(sum_cabin_bacon.index(min(sum_cabin_bacon))+1)