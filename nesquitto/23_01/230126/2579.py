N = int(input())
stairScore = []
dp = [0 for i in range(N)]
for i in range(N):
    stairScore.append(int(input()))

dp[0] = stairScore[0]
if N >= 2:
    dp[1] = stairScore[0] + stairScore[1]
if N >= 3:
    dp[2] = max(stairScore[0] + stairScore[2], stairScore[1] + stairScore[2])
if N >= 4:
    for i in range(3, N):
        dp[i] = max(dp[i-2] + stairScore[i], dp[i-3] + stairScore[i-1] + stairScore[i]) 

print(dp[N-1])