n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for max_k in range(n + 1): # 최대 길이
    cost = max_k**2 + (max_k + 1)**2
    for i in range(n): # 기준 X
        for j in range(n): # 기준 Y
            gold = 0
            # goldAxis = []
            for k in range(max_k+1): # 계산 k
                for mov_x in range(-k, k+1):
                    mov_y = k-abs(mov_x)
                    if n > i + mov_x >= 0 and n > j + mov_y >= 0:
                        if(grid[i + mov_x][j + mov_y] == 1):
                            gold += 1
                            # goldAxis.append([mov_x, mov_y, i + mov_x, j + mov_y])
                    mov_y = -mov_y
                    if mov_y != 0 and n > i + mov_x >= 0 and n > j + mov_y >= 0:
                        if(grid[i + mov_x][j + mov_y] == 1):
                            gold += 1
                            # goldAxis.append([mov_x, mov_y, i + mov_x, j + mov_y])
            total = gold * m - cost
            if total >= 0:
                if ans < gold:
                    ans = gold
                #     print(i, j, max_k)
                #     for q in goldAxis:
                #         print(q)
                # #ans = max(ans, gold)
                #     print(ans)
print(ans)

