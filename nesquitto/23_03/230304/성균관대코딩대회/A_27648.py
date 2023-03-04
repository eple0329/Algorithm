N, M, K = map(int, input().split())

min_K = N + M - 1
if min_K <= K:
    print('YES')
    for i in range(1, N+1):
        for j in range(M):
            print(i + j, end=' ')
        print()
else:
    print('NO')