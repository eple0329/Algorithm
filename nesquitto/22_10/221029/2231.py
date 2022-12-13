N = int(input())

solved = False
for i in range(N-1, 1, -1):
    strN = list(map(int, str(i)))
    makerNum = i + sum(strN)
    if makerNum == N:
        minMakerNum = i
        solved = True
if solved:
    print(minMakerNum)
else:
    print(0)