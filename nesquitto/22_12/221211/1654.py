K, N = map(int, input().split())
lanLine = []
for _ in range(K):
    lanLine.append(int(input()))

start = 0
end = max(lanLine)
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        break
    count = 0
    for i in lanLine:
        count += i//mid
    if count < N:
        end = mid-1
    else:
        start = mid+1
print(end)
