import math

def Prime(n):
    numberList = [True for _ in range(n+1)]
    numberList[0] = False
    numberList[1] = False
    returnList = []
    for i in range(2, math.floor(math.sqrt(n))+1):
        for j in range(2, 501):
            if i*j <=1000:
                numberList[i*j] = False
            else:
                break
    for i in range(1, 1001):
        if numberList[i]:
            returnList.append(i)
    return returnList

primeList = Prime(1000)
print(primeList)
N = int(input())
numList = list(map(int, input().split()))
tmp = 0
for i in numList:
    if i in primeList:
        tmp += 1
print(tmp)