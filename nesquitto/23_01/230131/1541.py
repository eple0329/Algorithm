mathematicalExpression = input()

num = []
symbol = []
plusedNum = []
for i in list(mathematicalExpression):
    if i  in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num.append(i)
    else:
        num.append(' ')
        symbol.append(i)
numList = list(map(int, ''.join(num).split()))
plusedNum.append(numList[0])

tmp = 0
isPlus = False
for idx, i in enumerate(symbol):
    if i == '+':
        if idx == 0:
            isPlus = True
        tmp += numList[idx+1]
    else:
        plusedNum.append(tmp)
        tmp = numList[idx+1]
plusedNum.append(tmp)
if '-' not in symbol:
    count = sum(plusedNum)
else:
    if isPlus:
        count = plusedNum[0] + plusedNum[1]
        for i in range(2, len(plusedNum)):
            count -= plusedNum[i]
    else:
        count = plusedNum[0]
        for i in range(1, len(plusedNum)):
            count -= plusedNum[i]
print(count)