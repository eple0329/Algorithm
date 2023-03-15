import sys
input = sys.stdin.readline

N = int(input().rstrip())
work_date = [tuple(map(int, input().split())) for i in range(N)]
dp = [0 for i in range(N)]

if work_date[0][0] == 1:
    dp[0] = work_date[0][1]
else:
    if work_date[0][0]-1 < N:
        dp[work_date[0][0]-1] = work_date[0][1]

for i in range(1, N):
    dp[i] = max(dp[i-1], dp[i])
    fin_date = i + work_date[i][0] - 1
    if fin_date < N:
        dp[fin_date] = max(dp[fin_date], dp[i-1] + work_date[i][1])
print(dp[N-1])
