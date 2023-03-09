N = int(input())
SEQUENCE = list(map(int, input().split()))

bigger = [0 for i in range(N)]
smaller = [0 for i in range(N)]

for idx in range(N):
    for i in range(idx):
        if SEQUENCE[idx] > SEQUENCE[i]:
            bigger[idx] = max(bigger[idx], bigger[i] + 1)
        if SEQUENCE[-(idx+1)] > SEQUENCE[-(i+1)]:
            smaller[-(idx+1)] = max(smaller[-(idx+1)], smaller[-(i+1)]+1)
    # -1 ~ -N
    
max_len = 0
for i in range(N):
    max_len = max(max_len, bigger[i] + smaller[i])
print(max_len+1)