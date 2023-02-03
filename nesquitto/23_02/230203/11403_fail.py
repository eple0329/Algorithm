import sys

N = int(sys.stdin.readline().rstrip())
G_MATRIX = [list(sys.stdin.readline().split()) for i in range(N)]
G_LIST = []
for i in range(N):
    for j in range(N):
        if G_MATRIX[i][j] == '1':
            G_LIST.append([i, j])

print_matrix = [['0' for _ in range(N)] for __ in range(N)]

for i in range(N):
    stack = [i]
    is_visited = []
    while stack:
        tmp = stack.pop()
        for j in G_LIST:
            if (j[0] in is_visited or j[0] is i) and j[1] not in is_visited:
                print_matrix[i][j[1]] = '1'
                stack.append(j[1])
                is_visited.append(j[1])
    for j in G_LIST:
        if j[1] == i and j[0] not in is_visited:
            print_matrix[i][i] = '0'
            
for i in range(N):
    print(" ".join(print_matrix[i]))