import math

def solve(num, i, befI):
    global minNumber
    if i == 4:
        return 0

    squareNum = int(math.sqrt(num)) # 해당 num으로 구할 수 있는 최대 제곱수
    if squareNum > befI:
        return 0
    if num - squareNum**2 == 0:
        minNumber = min(minNumber, i+1)
        return 0
    for j in range(squareNum, 0, -1):
        solve(num-j**2, i+1, j)
    

n = int(input())
minNumber = 100

solve(n, 0, 1000)
print(minNumber)