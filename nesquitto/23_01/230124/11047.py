import sys
N, K = map(int, sys.stdin.readline().split())
coinValues = []
for _ in range(N):
    coinValues.append(int(sys.stdin.readline().rstrip()))
coinValues.reverse()
numCoins = 0
for i in coinValues:
    numCoins += K//i
    K = K-((K//i)*i)

print(numCoins)