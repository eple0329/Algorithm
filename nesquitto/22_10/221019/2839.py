N = int(input().rstrip())
isSolved = False

for i in range(N//5, -1, -1):
    if (N-i*5)%3 == 0:
        print(i + (N-i*5)//3)
        isSolved = True
        break
if isSolved:
    pass
else:
    print(-1)