import sys

N, M = map(int, sys.stdin.readline().split())

invitedNode = [False for i in range(N+1)]
crossRoad = []
count = 0

for _ in range(M):
    crossRoad.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    if invitedNode[i]:
        continue
    count += 1
    stack = [i]
    while stack:
        popedNode = stack.pop()
        if invitedNode[popedNode]:
            continue
        invitedNode[popedNode] = True
        for j in crossRoad:
        #for k in range(len(crossRoad)-1, -1, -1):
        #    j = crossRoad[k]
            if j[0] == popedNode and not invitedNode[j[1]]:
                stack.append(j[1])
                #del(crossRoad[k])
            elif j[1] == popedNode and not invitedNode[j[0]]:
                stack.append(j[0])
                #del(crossRoad[k])
            else:
                pass

print(count)