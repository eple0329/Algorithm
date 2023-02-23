from heapq import heappop, heappush
import sys

heap = []
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if heap == []:
            print(0)
        else:
            print(heappop(heap) * -1)
    else:
        heappush(heap, (-1) * num)