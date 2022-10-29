import sys
N = int(sys.stdin.readline().rstrip())
strList = []
for i in range(N):
    strList.append(sys.stdin.readline().rstrip())
strList = sorted(set(strList))
for j in range(1, 51):
    for i in strList:
        if len(i) == j:
            print(i)