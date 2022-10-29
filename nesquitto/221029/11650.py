import sys


N = int(sys.stdin.readline().rstrip())
axis = []
for i in range(N):
    axis.append(list(map(int, sys.stdin.readline().split())))

axis.sort()
for i in axis:
    print(i[0], i[1])