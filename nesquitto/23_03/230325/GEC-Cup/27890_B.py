import math
X0, N = map(int, input().split())

for i in range(N):
    if X0 % 2 == 0:
        X0 = math.floor(X0 * 0.5) ^ 6
    else:
        X0 = (X0 * 2) ^ 6
print(X0)