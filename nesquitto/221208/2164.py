from collections import deque
N = int(input())
num = deque(_ for _ in range(1, N+1))
while len(num) != 1:
    num.popleft()
    if len(num) == 1:
        break
    num.append(num.popleft())

print(num[0])