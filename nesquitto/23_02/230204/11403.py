import sys

N = int(sys.stdin.readline().rstrip())
MATRIX_LIST = []
for _ in range(N):
    tmp_list = list(sys.stdin.readline().split())
    for i in range(N):
        if tmp_list[i] == '1':
            MATRIX_LIST.append((_, i))

matrix_return = [['0' for i in range(N)] for j in range(N)]
for i in range(N):
    stack = []
    is_visited = []
    for j in MATRIX_LIST:
        if i == j[0]:
            stack.append(j[1])
    while stack:
        tmp = stack.pop()
        if tmp not in is_visited:
            is_visited.append(tmp)
            matrix_return[i][tmp] = '1'
            for j in MATRIX_LIST:
                if tmp == j[0] and j[1] not in is_visited:
                    stack.append(j[1])
        else:
            continue
for i in matrix_return:
    print(" ".join(i))