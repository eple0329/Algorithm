import sys
N = int(sys.stdin.readline().rstrip())
num = [0 for i in range(10001)]
for i in range(N):
    num[int(sys.stdin.readline().rstrip())] += 1
for idx, i in enumerate(num):
    for j in range(i):
        print(idx)