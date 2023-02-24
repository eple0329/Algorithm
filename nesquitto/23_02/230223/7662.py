from heapq import heappop, heappush
import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    is_visited = [False for j in range(1000001)]
    num = int(sys.stdin.readline().rstrip())

    maxheap = []
    minheap = []
    for j in range(num):
        command = list(sys.stdin.readline().split())
        if command[0] == 'I':
            heappush(maxheap, -int(command[1]))
            heappush(minheap, int(command[1]))
            is_visited[int(command[1])] = True
        else:
            if maxheap == []:
                continue
            if command[1] == '1':
                pop_num = heappop(maxheap)
                is_visited[pop_num] = False
            else:
                pop_num = heappop(minheap)
                is_visited[pop_num] = False
    for idx in range(len(maxheap)-1, -1, -1):
        if is_visited[maxheap[idx]] == False:
            del(maxheap[idx])
    for idx in range(len(minheap)-1, -1, -1):
        if is_visited[minheap[idx]] == False:
            del(minheap[idx])
    if maxheap == []:
        print('EMPTY')
    else:
        print(maxheap)
        print(minheap)
        print(-heappop(maxheap), heappop(minheap))