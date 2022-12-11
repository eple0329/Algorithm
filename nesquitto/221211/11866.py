N, K = map(int, input().split())

circleList = [i for i in range(1, N+1)]
resultList = []
while len(circleList) != 0:
    for _ in range(K-1):
        circleList.append(circleList.pop(0))
    resultList.append(circleList.pop(0))
print('<' + ', '.join(map(str, resultList)) + '>')