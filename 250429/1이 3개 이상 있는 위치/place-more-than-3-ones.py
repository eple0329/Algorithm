n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


solve = 0
for i in range(n):
    for j in range(n):
        count = 0
        for dx, dy in dxdy:
            if n > i+dx >= 0 and n > j+dy >= 0:
                if grid[i+dx][j+dy] == 1:
                    count += 1
        if count >= 3:
            solve += 1
print(solve)