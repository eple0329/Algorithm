from heapq import heappop, heappush
import sys

N = int(sys.stdin.readline().rstrip())
heap = []

for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap == []:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))