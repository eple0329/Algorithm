from collections import deque

N, M = map(int, input().split())
is_visited = [False for i in range(200000)]
map = [0 for i in range(200000)]

queue = deque()
queue.append(N)
while queue:
    tmp = queue.popleft()
    if tmp == M:
        break
    if is_visited[tmp]:
        continue
    else:
        is_visited[tmp] = True
        if tmp * 2 < 109999:
            if not is_visited[tmp * 2] and map[tmp * 2] == 0:
                queue.append(tmp * 2)
                map[tmp * 2] = map[tmp] + 1
        if tmp - 1 != -1:
            if not is_visited[tmp - 1] and map[tmp - 1] == 0:                
                queue.append(tmp - 1)
                map[tmp - 1] = map[tmp] + 1
        if tmp + 1 <100100:
            if not is_visited[tmp + 1] and map[tmp + 1] == 0:                
                queue.append(tmp + 1)
                map[tmp + 1] = map[tmp] + 1
print(map[M])