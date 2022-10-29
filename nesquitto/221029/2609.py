a, b = map(int, input().split())
smallSameNum = -1
largeSameNum = -1
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        smallSameNum = i
        break
for i in range(1, b+1):
    if a * i % b == 0:
        largeSameNum = a * i
        break
print(smallSameNum)
print(largeSameNum)
