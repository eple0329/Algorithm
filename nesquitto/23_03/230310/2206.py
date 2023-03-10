import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

MATRIX_MAP = [list(map(int, input().rstrip())) for i in range(N)]
matrix_distance = [[[0] * 2 for i in range(M)] for j in range(N)]
matrix_distance[0][0][0] = 1 # 시작하는 칸도 포함이기 때문에
queue = deque()
queue.append((0, 0, 0))
found = False


DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1]
while queue:
    now_x, now_y, is_crashed = queue.popleft()
    if now_x == N-1 and now_y == M-1:
        print(matrix_distance[now_x][now_y][is_crashed])
        found = True
        break
    for i in range(4):
        next_x, next_y = now_x + DX[i], now_y + DY[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if MATRIX_MAP[next_x][next_y] == 1 and is_crashed == 0:
                matrix_distance[next_x][next_y][1] = matrix_distance[now_x][now_y][0] + 1
                queue.append((next_x, next_y, 1))
            elif MATRIX_MAP[next_x][next_y] == 0 and matrix_distance[next_x][next_y][is_crashed] == 0:
                matrix_distance[next_x][next_y][is_crashed] = matrix_distance[now_x][now_y][is_crashed] + 1
                queue.append((next_x, next_y, is_crashed))
if not found:
    print(-1)
