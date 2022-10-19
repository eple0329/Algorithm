N = int(input())
tmp = 1
for i in range(0, 10000):
    tmp += i * 6
    if tmp >= N:
        print(i+1)
        break