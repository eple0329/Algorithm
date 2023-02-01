# 해당 문제까지는 python 명명 권고사항을 따르지 않았습니다.

N = int(input())
squareData = []
isCheckSquare = [[False for _ in range(N)] for __ in range(N)]
tmp = [1, 2, 4, 8, 16, 32, 64, 128]
k = tmp.index(N)
for i in range(N):
    squareData.append(list(map(int, input().split())))

white = 0
blue = 0

def solve(startIdxX, startIdxY, length):
    global white
    global blue
    isSquared = True
    isRevSquared = True
    for i in range(startIdxX, startIdxX + length):
        for j in range(startIdxY, startIdxY + length):
            if squareData[i][j] == 0:
                isSquared = False
            else:
                isRevSquared = False
    if isSquared:
        blue += 1
        return
    elif isRevSquared:
        white += 1
        return
    else:            
        solve(startIdxX, startIdxY, length//2) # 0, 0
        solve(startIdxX + length//2, startIdxY, length//2) # 1, 0
        solve(startIdxX, startIdxY + length//2, length//2) # 0, 1
        solve(startIdxX + length//2, startIdxY + length//2, length//2) # 1, 1

solve(0, 0, N)
print(white)
print(blue)