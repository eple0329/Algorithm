T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queueList = list(map(int, input().split()))
    idxList = list(0 for i in range(N))
    idxList[M] = 1
    cnt = 0
    while True:
        if queueList[0] == max(queueList):
            cnt += 1
            if idxList[0] == 1:
                print(cnt)
                break
            else:
                queueList.pop(0)
                idxList.pop(0)

        else:
            queueList.append(queueList.pop(0))
            idxList.append(idxList.pop(0))
            
