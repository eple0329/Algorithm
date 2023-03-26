N = int(input())

one = 1
zero = 0
for i in range(N-1):
    tmp = one
    one = (one + zero)%15746
    zero = tmp % 15746
print((one + zero)%15746)
