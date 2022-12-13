testCase = int(input().rstrip())

for _ in range(testCase):
    parenthesis = list(str(input().rstrip()))
    checkNum = 0
    isCheck = True
    for i in parenthesis:
        if i == '(':
            checkNum += 1
        else:
            checkNum -= 1
        if checkNum < 0:
            print("NO")
            isCheck = False
            break
    if isCheck and checkNum == 0:
        print("YES")
    elif isCheck:
        print("NO")