import heapq
import sys

heap = []

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)

