import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomato_box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            queue.append([i, j])
while queue:
    x, y = queue.popleft()
    for k in range(4):
        move_x, move_y = x+DX[k], y+DY[k]
        if 0 <= move_x < N and 0 <= move_y < M:
            if tomato_box[move_x][move_y] == 0:
                tomato_box[move_x][move_y] = tomato_box[x][y] + 1
                queue.append([move_x, move_y])
is_cannot_ripen = False
for i in tomato_box:
    if 0 in i:
        is_cannot_ripen = True
        print(-1)
        break
if not is_cannot_ripen:
    print(max(map(max, tomato_box))-1)