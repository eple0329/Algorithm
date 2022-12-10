L = int(input())
string = input()
r = 31
M = 1234567891
res = 0
for i in range(len(string)):
    res += (ord(string[i])-96)*(r**(i))
print(res%M)