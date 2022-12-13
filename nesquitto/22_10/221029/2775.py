T = int(input())

apt = [[i for i in range(15)] for j in range(15)]
for i in range(1, 15):
    for j in range(2, 15):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apt[k][n])
