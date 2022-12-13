
n = int(input())
isSeq = True
count = 1
ret = []
stack = []
for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        ret.append("+")
        count += 1
    if stack[-1] == num:
        ret.append("-")
        stack.pop()
    else:
        isSeq = False
        break
if isSeq:
    for i in ret:
        print(i)
else:
    print("NO")
