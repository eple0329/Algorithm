N = int(input())

RGB_HOME = [list(map(int, input().split())) for i in range(N)]
dp_home = [[0 for i in range(3)] for j in range(N)]

dp_home[0] = RGB_HOME[0]

for i in range(1, N):
    dp_home[i][0] = min(dp_home[i-1][1]+RGB_HOME[i][0], dp_home[i-1][2] + RGB_HOME[i][0])
    dp_home[i][1] = min(dp_home[i-1][0]+RGB_HOME[i][1], dp_home[i-1][2] + RGB_HOME[i][1])
    dp_home[i][2] = min(dp_home[i-1][1]+RGB_HOME[i][2], dp_home[i-1][0] + RGB_HOME[i][2])

print(min(dp_home[N-1]))

