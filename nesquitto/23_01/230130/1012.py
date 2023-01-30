import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbageField = [[False for i in range(N)] for j in range(M)]
    isCheckedField = [[False for i in range(N)] for j in range(M)]
    count = 0
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        cabbageField[x][y] = True
    
    for i in range(M):
        for j in range(N):
            if cabbageField[i][j] and not isCheckedField[i][j]:
                stack = []
                count += 1
                stack.append((i, j))
                while stack:
                    tmpAxis = stack.pop()
                    isCheckedField[tmpAxis[0]][tmpAxis[1]] = True
                    #상
                    if tmpAxis[0] != 0:
                        if cabbageField[tmpAxis[0]-1][tmpAxis[1]] and not isCheckedField[tmpAxis[0]-1][tmpAxis[1]]:
                            stack.append((tmpAxis[0]-1, tmpAxis[1]))
                    #하
                    if tmpAxis[0] != M-1:
                        if cabbageField[tmpAxis[0]+1][tmpAxis[1]] and not isCheckedField[tmpAxis[0]+1][tmpAxis[1]]:
                            stack.append((tmpAxis[0]+1, tmpAxis[1]))
                    #좌
                    if tmpAxis[1] != 0:
                        if cabbageField[tmpAxis[0]][tmpAxis[1]-1] and not isCheckedField[tmpAxis[0]][tmpAxis[1]-1]:
                            stack.append((tmpAxis[0], tmpAxis[1]-1))
                    #우
                    if tmpAxis[1] != N-1:
                        if cabbageField[tmpAxis[0]][tmpAxis[1]+1] and not isCheckedField[tmpAxis[0]][tmpAxis[1]+1]:
                            stack.append((tmpAxis[0], tmpAxis[1]+1))
            else:
                continue
    print(count)
