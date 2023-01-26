import sys
N, M  = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(numList)):
    numList[i] += numList[i-1]

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        print(numList[end-1])
    else:
        print(numList[end-1]-numList[start-2])
