import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M, X = map(int, input().split())

distance = dict()
for i in range(1, N+1):
    distance[i] = []

for i in range(M):
    st, en, co = map(int, input().split())
    distance[st].append((co, en))

cost_to_x = [-1 for i in range(N+1)]

def dijkstra(start, end):
    if start == end:
        return 0
    heap = []
    min_distance = [1000000 for i in range(N+1)]
    min_distance[start] = 0
    for i in distance[start]:
        heappush(heap, i)
    while heap:
        now_cost, now_node = heappop(heap)
        if now_node == end:
            return now_cost

        if min_distance[now_node] > now_cost:
            min_distance[now_node] = now_cost
            for i in distance[now_node]:
                next_cost, next_node = i
                heappush(heap, (now_cost + next_cost, next_node))
    return -1

def dijkstra_list(start):
    heap = []
    min_distance = [1000000 for i in range(N+1)]
    min_distance[start] = 0
    for i in distance[start]:
        heappush(heap, i)
    while heap:
        now_cost, now_node = heappop(heap)

        if min_distance[now_node] > now_cost:
            min_distance[now_node] = now_cost
            for i in distance[now_node]:
                next_cost, next_node = i
                heappush(heap, (now_cost + next_cost, next_node))
    return min_distance

for i in range(1, N+1):
    if X == i:
        cost_to_x[i] = -100000
    else:
        cost_to_x[i] = dijkstra(i, X)

tmp_list = dijkstra_list(X)
for i in range(1, len(tmp_list)):
    cost_to_x[i] += tmp_list[i]

print(max(cost_to_x))