import sys

N = int(sys.stdin.readline().rstrip())
N_GRID = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

is_visited = [[False for i in range(N)] for j in range(N)]
district = dict()
district['R'] = 0
district['G'] = 0
district['B'] = 0
district['RG'] = 0
for i in range(N):
    for j in range(N):
        if not is_visited[i][j]:
            now_color = N_GRID[i][j]
            district[now_color] += 1
            stack = [[i, j]]
            while stack:
                tmp = stack.pop()
                x, y = tmp[0], tmp[1]
                is_visited[x][y] = True
                for k in range(4):
                    move_x = x + DX[k]
                    move_y = y + DY[k]
                    if 0 <= move_x < N and 0 <= move_y < N:
                        if not is_visited[move_x][move_y]:
                            if N_GRID[move_x][move_y] == now_color:
                                stack.append([move_x, move_y])
is_visited = [[False for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if not is_visited[i][j]:
            now_color = N_GRID[i][j]
            if now_color == 'B':
                is_visited[i][j] = True
                continue
            district['RG'] += 1
            stack = [[i, j]]
            while stack:
                tmp = stack.pop()
                x, y = tmp[0], tmp[1]
                is_visited[x][y] = True
                for k in range(4):
                    move_x = x + DX[k]
                    move_y = y + DY[k]
                    if 0 <= move_x < N and 0 <= move_y < N:
                        if not is_visited[move_x][move_y]:
                            if N_GRID[move_x][move_y] != "B":
                                stack.append([move_x, move_y])
print(district['R'] + district['G'] + district['B'], district['B'] + district['RG'])