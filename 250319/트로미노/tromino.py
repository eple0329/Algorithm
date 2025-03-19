N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
move = [
    ((-1, 0), (0, -1)),
    ((-1, 0), (1, 0)),
    ((-1, 0), (0, 1)),
    ((0, -1), (1, 0)),
    ((0, -1), (0, 1)),
    ((1, 0), (0, 1)),
    ((-1, -1), (-1, 0)), # 안해도 될듯
    ((-1, 0), (-1, 1)),
    ((-1, 1), (0, 1)),
    ((0, 1), (1, 1)),
    ((1, 1), (1, 0)),
    ((1, -1), (0, -1)),
    ((0, -1), (-1, -1)) # 안해도 될듯
    ]

global_max = 0
for i in range(N):
    for j in range(M):
        now = grid[i][j]
        for tmp1, tmp2 in move:
            tmp_max = now
            if i + tmp1[0] < 0 or i + tmp1[0] >= N or j + tmp1[1] < 0 or j + tmp1[1] >= M:
                continue
            if i + tmp2[0] < 0 or i + tmp2[0] >= N or j + tmp2[1] < 0 or j + tmp2[1] >= M:
                continue
                
            tmp_max += grid[i + tmp1[0]][j + tmp1[1]]
            tmp_max += grid[i + tmp2[0]][j + tmp2[1]]
            
            global_max = max(global_max, tmp_max)
print(global_max)


