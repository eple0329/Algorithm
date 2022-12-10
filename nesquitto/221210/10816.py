N = int(input())
NList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))

resDict = dict()
result = list()

for i in NList:
    if i in resDict.keys():
        resDict[i] += 1
    else:
        resDict[i] = 1
for i in MList:
    if i in resDict.keys():
        result.append(resDict[i])
    else:
        result.append(0)
print(' '.join(map(str, result)))
