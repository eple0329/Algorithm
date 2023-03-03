import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

bus_info = [[] for i in range(N+1)]
for i in range(M):
    bus_start, bus_end, bus_cost = map(int, sys.stdin.readline().split())
    bus_info[bus_start].append((bus_cost, bus_end))

start, end = map(int, sys.stdin.readline().split())
cost_to_end = [1000000000 for i in range(N+1)]
heap = []
heappush(heap, (0, start))
is_visit = []
while heap:
    cost, node = heappop(heap)
    if cost_to_end[node] <= cost:
        continue
    cost_to_end[node] = cost
    for i in bus_info[node]:
        bus_cost, bus_end = i
        heappush(heap, (cost_to_end[node] + bus_cost, bus_end))

print(cost_to_end[end])