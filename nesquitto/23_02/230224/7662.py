from heapq import heappop, heappush
import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    
    num = int(sys.stdin.readline().rstrip())
    is_visited = [False] * num
    maxheap = []
    minheap = []

    for j in range(num):
        command = list(sys.stdin.readline().split())
        if command[0] == 'I':
            heappush(maxheap, (-int(command[1]), j))
            heappush(minheap, (int(command[1]), j))
            is_visited[j] = True
        else:
            if command[1] == '1':
                while maxheap and not is_visited[maxheap[0][1]]:
                    heappop(maxheap)
                if maxheap:
                    idx = heappop(maxheap)[1]
                    is_visited[idx] = False
            else:
                while minheap and not is_visited[minheap[0][1]]:
                    heappop(minheap)
                if minheap:
                    idx = heappop(minheap)[1]
                    is_visited[idx] = False
                
    
    while maxheap and is_visited[maxheap[0][1]] == False:
        heappop(maxheap)
    while minheap and is_visited[minheap[0][1]] == False:
        heappop(minheap)
    if maxheap == []:
        print('EMPTY')
    else:
        print(-heappop(maxheap)[0], heappop(minheap)[0])