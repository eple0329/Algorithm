import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline
N, M = map(int, input().split())

LAB_MAP = [list(map(int, input().split())) for i in range(N)]
empty_space = []
max_space = 0

def solve(data_map_, data_wall):
    data_map = deepcopy(data_map_)
    for i in data_wall:
        data_map[i[0]][i[1]] = 1
    queue = deque()
    for i in range(N):
        for j in range(M):
            if data_map[i][j] == 2:
                queue.append((i, j))
    while queue:
        now_location_x, now_location_y = queue.popleft()
        DX, DY = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            next_location_x = now_location_x + DX[i]
            next_location_y = now_location_y + DY[i]
            if 0 <= now_location_x + DX[i] < N and 0 <= now_location_y + DY[i] < M:
                if data_map[next_location_x][next_location_y] == 0:
                    data_map[next_location_x][next_location_y] = 2
                    queue.append((next_location_x, next_location_y))
    result = 0
    for i in data_map:
        for j in i:
            if j == 0:
                result += 1
    global max_space
    max_space = max(result, max_space)




for i in range(N):
    for j in range(M):
        if LAB_MAP[i][j] == 0:
            empty_space.append((i, j))

for i in list(combinations(empty_space, 3)):
    solve(LAB_MAP[:], i)

print(max_space)