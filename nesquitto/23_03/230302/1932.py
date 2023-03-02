N = int(input())

TRIANGLE_NUM = [list(map(int, input().split())) for i in range(N)]
dp = [[0 for j in range(i+1)] for i in range(N)]

dp[0][0] = TRIANGLE_NUM[0][0]
for i in range(N-1):
    for j in range(i+1):
        if dp[i+1][j] == 0:
            dp[i+1][j] = dp[i][j] + TRIANGLE_NUM[i+1][j]
        else:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + TRIANGLE_NUM[i+1][j])
        if dp[i+1][j+1] == 0:
            dp[i+1][j+1] = dp[i][j] + TRIANGLE_NUM[i+1][j+1]
        else:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + TRIANGLE_NUM[i+1][j+1])

print(max(dp[N-1]))