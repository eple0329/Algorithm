N = int(input())
NList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))

NList = sorted(NList)
for i in MList:
    start = 0
    end = len(NList)-1
    find = False
    while start <= end:
        mid = (start + end) // 2
        if NList[mid] > i:
            end = mid - 1
        elif NList[mid] < i:
            start = mid + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)

