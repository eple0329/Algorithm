import sys

N, M = map(int, sys.stdin.readline().split())
pocketMon = dict()
for _ in range(N):
    data = sys.stdin.readline().rstrip()
    pocketMon[data] = _+1
    pocketMon[str(_+1)] = data
for _ in range(M):
    print(pocketMon[sys.stdin.readline().rstrip()])