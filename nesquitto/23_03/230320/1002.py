from math import sqrt

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    R = sqrt((x2-x1) ** 2 + (y2-y1)**2)
    if R == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == R or r1+r2 == R:
        print(1)
    elif abs(r1-r2) < R < r1+r2:
        print(2)
    else:
        print(0)
