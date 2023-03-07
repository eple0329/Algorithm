from heapq import heappop, heappush
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input().rstrip())

distance_to_node = [40000000 for i in range(V+1)]
cost_to_node = dict()
heap = []

for i in range(E):
    start, end, cost = map(int, input().split())
    if start in cost_to_node.keys():
        cost_to_node[start].append((cost, end))
    else:
        cost_to_node[start] = [(cost, end)]

distance_to_node[K] = 0
heappush(heap, (0, K))
while heap:
    now_cost, now_end = heappop(heap)
    if now_end in cost_to_node.keys():
        can_go_node = cost_to_node[now_end]
        for i in can_go_node:
            next_cost, next_node = i
            distance_to_node[next_node] = min(distance_to_node[next_node], now_cost + next_cost)
            heappush(heap, (distance_to_node[next_node], next_node))
        del cost_to_node[now_end]

for i in range(1, V+1):
    if distance_to_node[i] == 40000000:
        print("INF")
    else:
        print(distance_to_node[i])