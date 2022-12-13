import sys


N = int(sys.stdin.readline().rstrip())
memberList = []
for i in range(N):
    a, b = sys.stdin.readline().split()
    memberList.append((int(a), b))
for i in sorted(memberList, key=lambda x: x[0]):
    print(i[0], i[1])