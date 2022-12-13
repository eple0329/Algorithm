N, M, B = map(int, input().split())

mapList = []
for _ in range(N):
    mapList += list(map(int, input().split()))
maxHeight = max(mapList)
targetHeight = maxHeight # 최대높이에서부터 아래로 점점...

needTime = 100000000
needHeight = 1000000

while targetHeight >= 0: # 계에에에속 확인하기
    needBlock = 0
    destroyBlock = 0
    for i in mapList:
        if i > targetHeight:
            destroyBlock += i - targetHeight
        else:
            needBlock += targetHeight - i
    if needBlock <= destroyBlock + B:
        tmpTime = needBlock + destroyBlock * 2
        if needTime > tmpTime:
            needTime = tmpTime
            needHeight = targetHeight
    targetHeight -= 1
print(needTime, needHeight)