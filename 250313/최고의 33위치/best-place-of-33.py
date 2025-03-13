n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_coin = 0
for i in range(len(grid)-2):
    for j in range(len(grid[i])-2):
        tmp_coin = 0
        for x in range(3):
            for y in range(3):
                if grid[i+x][j+y] == 1:
                    tmp_coin += 1
        if max_coin < tmp_coin:
            max_coin = tmp_coin

print(max_coin)