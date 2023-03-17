import sys
input = sys.stdin.readline

N, K = map(int, input().split())
thing_info = [(map(int, input().split())) for i in range(N)]
dp =[[0 for j in range(K+1)] for i in range(N+1)]

for i in range(1, N+1):
    thing_w, thing_v = thing_info[i-1]
    for j in range(1, K+1):
        if j  >= thing_w:
            dp[i][j] = max(dp[i-1][j-thing_w] + thing_v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])