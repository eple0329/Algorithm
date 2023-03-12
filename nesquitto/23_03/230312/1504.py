from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
distance = dict()
for i in range(N):
    distance[i+1] = []
for i in range(E):
    a, b, c = map(int, input().split())
    distance[a].append((c, b))
    distance[b].append((c, a))
u, v = map(int, input().split())

#(1 -> a) + (a -> b) + (b -> N)
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



result = 10000000
u_to_v = dijkstra(u, v)
if u_to_v != -1:
    to_u = dijkstra(1, u)
    if to_u != -1:
        v_to_N = dijkstra(v, N)
        if v_to_N != -1:
            result = u_to_v + to_u + v_to_N

    to_v = dijkstra(1, v)
    if to_v != -1:
        u_to_N = dijkstra(u, N)
        if u_to_N != -1:
            result = min(result, u_to_v + to_v + u_to_N)


if result == 10000000:
    print(-1)
else:
    print(result)