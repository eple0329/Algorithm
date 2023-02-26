N = int(input())

NUM_LIST = list(map(int, input().split()))
dp = [0 for i in range(N)]
dp[0] = 1

for i in range(1, N):
    now_idx = NUM_LIST[i]
    for j in range(i-1, -1, -1):
        if now_idx > NUM_LIST[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] == 0: 
        dp[i] = 1
print(max(dp))