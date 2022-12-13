N, M = map(int, input().split())
map = []
min = 100
for _ in range(N):
    map.append(list(input()))
for i in range(0, N-7):
    for j in range(0, M-7):
        num = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if map[k][l] == 'W' and (k + l) % 2 == 0:
                    num += 1
                elif map[k][l] == 'B' and (k + l) % 2 == 1:
                    num += 1
        if num > 32:
            num = 64 - num
        if num < min:
            min = num
print(min)