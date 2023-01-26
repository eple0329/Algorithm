N = int(input())

num = 1
for i in range(2, N+1):
    num *= i

numlist =list(str(num))
numlist.reverse()
cnt = 0
for i in numlist:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)