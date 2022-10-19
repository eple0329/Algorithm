N, M = map(int, input().split())
numList = list(map(int, input().split()))
maxNum = -1
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sumNum = numList[i] + numList[j] + numList[k]
            if sumNum > maxNum and sumNum <= M:
                maxNum = sumNum
print(maxNum)
