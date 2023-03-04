from collections import deque

N, M = map(int, input().split())
spot_num = [-1 for i in range(100001)]
spot_num[N] = 0

queue = deque()
queue.append(N)
while queue:
    now_num = queue.popleft()
    now_distance = spot_num[now_num]
    if now_num == M:
        print(now_distance)
        break

    if now_num * 2 <= 100000 and spot_num[now_num * 2] == -1: 
        spot_num[now_num * 2] = now_distance
        queue.appendleft(now_num * 2)

    if 0 <= now_num - 1 <= 100000 and spot_num[now_num - 1] == -1:
        spot_num[now_num - 1] = now_distance + 1
        queue.append(now_num - 1)

    if 0 <= now_num + 1 <= 100000 and spot_num[now_num + 1] == -1:
        spot_num[now_num + 1] = now_distance + 1
        queue.append(now_num + 1)