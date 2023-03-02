T = int(input())

for _ in range(T):
    N = int(input())
    STICKER_DATA = [list(map(int, input().split())) for i in range(2)]
    dp = [[0 for i in range(N)] for j in range(2)]
    if N == 1:
        print(max(STICKER_DATA[0][0], STICKER_DATA[1][0]))
        continue
    if N == 2:
        print(max(STICKER_DATA[0][0] + STICKER_DATA[1][1], STICKER_DATA[1][0] + STICKER_DATA[0][1]))
        continue
    dp[0][0] = STICKER_DATA[0][0]
    dp[1][0] = STICKER_DATA[1][0]
    dp[0][1] = STICKER_DATA[0][1] + dp[1][0]
    dp[1][1] = STICKER_DATA[1][1] + dp[0][0]
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-2] + STICKER_DATA[0][i], dp[0][i-2] + STICKER_DATA[1][i-1] + STICKER_DATA[0][i], dp[1][i-1] + STICKER_DATA[0][i])
        dp[1][i] = max(dp[0][i-2] + STICKER_DATA[1][i], dp[1][i-2] + STICKER_DATA[0][i-1] + STICKER_DATA[1][i], dp[0][i-1] + STICKER_DATA[1][i])
    print(max(max(dp[0]), max(dp[1])))