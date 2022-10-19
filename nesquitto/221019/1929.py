import math

def Prime(n):
    if n == 1:
        return []
    numberList = [True for _ in range(n+1)]
    numberList[0] = False
    numberList[1] = False
    returnList = []
    for i in range(2, math.floor(math.sqrt(n))+1):
        for j in range(2, n//2+1):
            if i*j <n+1 and numberList[i]:
                numberList[i*j] = False
            else:
                break
    for i in range(1, n+1):
        if numberList[i]:
            returnList.append(i)
    return returnList

M, N = map(int, input().split())
for i in Prime(N):
    if i >= M:
        print (i)