N, M = map(int, input().split())
PAPER_MAP = [list(map(int, input().split())) for i in range(N)]
max_of_sum = -1
for i in range(N):
    for j in range(M):
        start = PAPER_MAP[i][j]
        
        if i + 1 < N and j + 1 < M:
        # oo
        # oo
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j] + PAPER_MAP[i][j+1] + PAPER_MAP[i+1][j+1])

        
        if i + 3 < N:
        # oooo
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j] + PAPER_MAP[i+2][j] + PAPER_MAP[i+3][j])

        
        if j + 3 < M:
        # o
        # o
        # o
        # o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i][j+1] + PAPER_MAP[i][j+2] + PAPER_MAP[i][j+3])
        
        
        if i + 2 < N and j + 1 < M:
        # o
        # o
        # oo
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j] + PAPER_MAP[i+2][j] + PAPER_MAP[i+2][j+1])
        # oo
        # o
        # o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j] + PAPER_MAP[i+2][j] + PAPER_MAP[i][j+1])
        # oo
        #  o
        #  o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+2][j+1] + PAPER_MAP[i][j+1])
        #  o
        #  o
        # oo
            max_of_sum = max(max_of_sum, PAPER_MAP[i][j+1] + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+2][j] + PAPER_MAP[i+2][j+1])
        # o
        # oo
        # o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j] + PAPER_MAP[i+2][j] + PAPER_MAP[i+1][j+1])
        #  o
        # oo
        #  o
            max_of_sum = max(max_of_sum, PAPER_MAP[i][j+1] + PAPER_MAP[i+1][j] + PAPER_MAP[i+2][j+1] + PAPER_MAP[i+1][j+1])
        #  o
        # oo
        # o
            max_of_sum = max(max_of_sum, PAPER_MAP[i][j+1] + PAPER_MAP[i+1][j] + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+2][j])
        # o
        # oo
        #  o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j] + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+2][j+1])
        
        if i + 1 < N and j + 2 < M:
        # ooo
        # o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i][j+1] + PAPER_MAP[i][j+2] + PAPER_MAP[i+1][j])    
        # ooo
        #   o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i][j+1] + PAPER_MAP[i][j+2] + PAPER_MAP[i+1][j+2])
        # o
        # ooo
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+1][j+2] + PAPER_MAP[i+1][j])
        #   o
        # ooo
            max_of_sum = max(max_of_sum, PAPER_MAP[i][j+2] + PAPER_MAP[i+1][j] + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+1][j+2])
        # ooo
        #  o
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i][j+1] + PAPER_MAP[i][j+2] + PAPER_MAP[i+1][j+1])
        #  o
        # ooo
            max_of_sum = max(max_of_sum, PAPER_MAP[i][j+1] + PAPER_MAP[i+1][j] + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+1][j+2])
        # oo
        #  oo
            max_of_sum = max(max_of_sum, start + PAPER_MAP[i][j+1] + PAPER_MAP[i+1][j+1] + PAPER_MAP[i+1][j+2])
        #  oo
        # oo
            max_of_sum = max(max_of_sum, PAPER_MAP[i][j+1] + PAPER_MAP[i+1][j] + PAPER_MAP[i+1][j+1] + PAPER_MAP[i][j+2])

print(max_of_sum)