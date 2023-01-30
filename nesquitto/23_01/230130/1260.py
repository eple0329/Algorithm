import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
crossLine = []
for i in range(M):
    crossLine.append(list(map(int, sys.stdin.readline().split())))

def DFS(crossLine, V):
    isVisited = []
    stack = deque()
    stack.append(V)
    while stack:
        stackTmp = []
        visitNode = stack.pop()
        if visitNode in isVisited:
            continue
        isVisited.append(visitNode)
        for i in crossLine:
            if i[0] == visitNode:
                stackTmp.append(i[1])
            elif i[1] == visitNode:
                stackTmp.append(i[0])
            else:
                pass
        stackTmp.sort(reverse=True)
        stack += stackTmp
    print(' '.join(map(str, isVisited)))

def BFS(crossLine, V):
    isVisited = []
    queue = deque()
    queue.append(V)
    while queue:
        queueTmp = []
        visitNode = queue.popleft()
        if visitNode in isVisited:
            continue
        isVisited.append(visitNode)
        for i in crossLine:
            if i[0] == visitNode:
                queueTmp.append(i[1])
            elif i[1] == visitNode:
                queueTmp.append(i[0])
            else:
                pass
        queueTmp.sort(reverse=False)
        queue += queueTmp
    print(' '.join(map(str, isVisited)))

DFS(crossLine, V)
BFS(crossLine, V)
