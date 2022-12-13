N = int(input())
P = list(map(int, input().split()))

totalSpendTime = 0
lastPersonTime = 0
for i in sorted(P):
    totalSpendTime = totalSpendTime + lastPersonTime + i
    lastPersonTime += i

print(totalSpendTime)