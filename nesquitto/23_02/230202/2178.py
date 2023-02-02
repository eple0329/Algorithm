import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze_list = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

START_AXIS_X, START_AXIS_Y = 0, 0
END_AXIS_X, END_AXIS_Y = N-1, M-1
DIFFERENCE_X = (0, 0, 1, -1)
DIFFERENCE_Y = (1, -1, 0, 0)

queue = deque()
queue.append((START_AXIS_X, START_AXIS_Y))
while queue:
    axis_x, axis_y = queue.popleft()
    if axis_x == END_AXIS_X and axis_y == END_AXIS_Y:
        break
    for i in range(4):
        next_x = axis_x + DIFFERENCE_X[i]
        next_y = axis_y + DIFFERENCE_Y[i]
        if 0 <= next_x < N and 0 <= next_y < M and maze_list[next_x][next_y] == 1:
            queue.append((next_x, next_y))
            maze_list[next_x][next_y] = maze_list[axis_x][axis_y] + 1
    
    
print(maze_list[END_AXIS_X][END_AXIS_Y])