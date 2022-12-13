import sys
N = int(input().rstrip())
numList = list()
for i in range(N):
    numList.append(int(sys.stdin.readline().rstrip()))
for i in sorted(numList):
    print(i)
