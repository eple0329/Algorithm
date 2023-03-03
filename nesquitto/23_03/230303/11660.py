import sys

N, M = map(int, sys.stdin.readline().split())

NUM_MATRIX = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
NUM_SUM_MATRIX = [[0 for i in range(N)] for j in range(N)]
NUM_SUM_MATRIX[0][0] = NUM_MATRIX[0][0]
for i in range(1, N):
    NUM_SUM_MATRIX[i][0] = NUM_SUM_MATRIX[i-1][0] + NUM_MATRIX[i][0]
    NUM_SUM_MATRIX[0][i] = NUM_SUM_MATRIX[0][i-1] + NUM_MATRIX[0][i]
for i in range(1, N):
    for j in range(1, N):
        NUM_SUM_MATRIX[i][j] = NUM_SUM_MATRIX[i][j-1] + NUM_SUM_MATRIX[i-1][j] - NUM_SUM_MATRIX[i-1][j-1] + NUM_MATRIX[i][j]

for i in range(M):

    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    if x1 == 0:
        if y1 == 0:
            print(NUM_SUM_MATRIX[x2][y2])
        else:
            print(NUM_SUM_MATRIX[x2][y2]-NUM_SUM_MATRIX[x2][y1-1])
    else:
        if y1 == 0:
            print(NUM_SUM_MATRIX[x2][y2]-NUM_SUM_MATRIX[x1-1][y2])
        else:
            print(NUM_SUM_MATRIX[x2][y2]-NUM_SUM_MATRIX[x2][y1-1]-NUM_SUM_MATRIX[x1-1][y2] + NUM_SUM_MATRIX[x1-1][y1-1])