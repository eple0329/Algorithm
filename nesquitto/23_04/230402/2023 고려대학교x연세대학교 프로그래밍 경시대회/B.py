from heapq import heappop, heappush
N = int(input())
axis = list(map(int, input().split()))
axis_heap = []
even_min = 2000000001
odd_min = 2000000001
for i in axis:
    heappush(axis_heap, i)
tmp_bef = heappop(axis_heap)
for i in range(N-1):
    tmp_aft = heappop(axis_heap)
    if (abs(tmp_aft-tmp_bef))%2 == 1:
        odd_min = min(odd_min, abs(tmp_aft-tmp_bef))
    else:
        even_min = min(even_min, abs(tmp_aft-tmp_bef))
    tmp_bef = tmp_aft
if even_min == 2000000001:
    print(-1, end=" ")
else:
    print(even_min, end=" ")
if odd_min == 2000000001:
    print(-1)
else:
    print(odd_min)