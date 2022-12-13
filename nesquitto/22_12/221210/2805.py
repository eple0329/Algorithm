N, M = map(int, input().split())
hList = list(map(int, input().split()))

small = 0
big = max(hList)
while small <= big:
    mid = (big+small)//2
    MCheck = 0
    for i in hList:
        if mid < i:
            MCheck += (i-mid)
    if MCheck < M:
        big  = mid-1
    else:
        small = mid+1

print(big)
