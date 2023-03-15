import sys
input = sys.stdin.readline

N = int(input().rstrip())
work_date = [tuple(map(int, input().split())) for i in range(N)]

dp = [0 for i in range(N)]

for i in range(work_date[0][0]-1, N):
    dp[i] = work_date[0][1]

for i in range(1, N):
    for j in range(i + work_date[i][0]-1, N):
        tmp = dp[i-1] + work_date[i][1]
        if dp[j] >= tmp:
            break
        else:
            dp[j] = tmp

print(dp[N-1])