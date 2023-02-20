import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
tomato_box = []
for __ in range(H):
    tomato_box.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_box[i][j][k] == 1:
                queue.append([i, j, k])

d_h, d_y, d_x = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
while queue:
    now_h, now_y, now_x = queue.popleft()
    date_ripen = tomato_box[now_h][now_y][now_x]
    for _ in range(6):
        if 0 <= now_h+d_h[_] < H and 0 <= now_y+d_y[_] < N and 0 <= now_x+d_x[_] < M:
            if tomato_box[now_h+d_h[_]][now_y+d_y[_]][now_x+d_x[_]] == 0:
                tomato_box[now_h+d_h[_]][now_y+d_y[_]][now_x+d_x[_]] = date_ripen + 1
                queue.append([now_h+d_h[_], now_y+d_y[_], now_x+d_x[_]])

result = -1
for i in range(H):
    if result == 0:
        break
    for j in range(N):
        if result == 0:
            break
        for k in range(M):
            if tomato_box[i][j][k] == 0:
                result = 0
                break
            else:
                result = max(result, tomato_box[i][j][k])
print(result - 1)