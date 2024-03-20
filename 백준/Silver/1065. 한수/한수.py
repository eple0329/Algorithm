N = int(input())

count = 0
for i in range(1, N+1):
    num = str(i)
    numLen = len(str(i))
    if(numLen <= 2):
        count += 1
    else:
        dif = int(num[0]) - int(num[1])
        for j in range(1, numLen-1):
            if(int(num[j]) - int(num[j+1]) != dif):
                break;
            if(j == numLen-2):
                count += 1
print(count)