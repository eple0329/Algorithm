n = int(input())

data=[]
data.append(1)
data.append(2)
data.append(3)
for i in range(n-1):
    data.append(data[-1]+data[-2])
print(data[n-1]%10007)