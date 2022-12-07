from collections import deque

K = int(input())
tmp = deque()
sum = 0
for _ in range(K):
    n = int(input())
    if n == 0:
        m = tmp.pop()
        sum -= m
    else:
        sum += n
        tmp.append(n)
print(sum)
