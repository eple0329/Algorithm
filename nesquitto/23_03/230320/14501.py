N = int(input())
counsel = [(map(int, input().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(1, N+1):
    T, P = counsel[i-1]
    dp[i] = max(dp[i], dp[i-1])
    if i+T-1 <= N:
        dp[i+T-1] = max(dp[i+T-1], dp[i-1] + P)
    #print(dp)

print(dp[N])