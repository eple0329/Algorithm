N = int(input())
numList = list(map(int, input().split()))

for i in range(N):
    numList[i] = [i, numList[i], 0]

numList = sorted(numList, key=lambda x:x[1])

nowNum = numList[0][1]
count = 0
for i in range(N):
    if numList[i][1] == nowNum:
        numList[i][2] = count
    elif numList[i][1] > nowNum:
        count += 1
        numList[i][2] = count
        nowNum = numList[i][1]
    else:
        pass

numList = sorted(numList, key=lambda x:x[0])

for i in numList:
    print(str(i[2]), end=' ')