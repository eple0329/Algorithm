import sys

computerN = int(sys.stdin.readline().rstrip())
crossLineN = int(sys.stdin.readline().rstrip())
crossLine = []
nodeToBeCheck = []
isVirusedComputer = [False for i in range(computerN+1)]
isVirusedComputer[0] = True
isVirusedComputer[1] = True
virusedComputerN = 0

for _ in range(crossLineN):
    checkedLine = list(map(int, sys.stdin.readline().split()))
    if 1 in checkedLine:
        if checkedLine[0] == 1:
            if not isVirusedComputer[checkedLine[1]]:
                virusedComputerN += 1
                nodeToBeCheck.append(checkedLine[1])
                isVirusedComputer[checkedLine[1]] = True
        else:
            if not isVirusedComputer[checkedLine[0]]:
                virusedComputerN += 1
                nodeToBeCheck.append(checkedLine[0])
                isVirusedComputer[checkedLine[0]] = True
        continue
    crossLine.append(checkedLine)
while nodeToBeCheck:
    popNum = nodeToBeCheck.pop()
    idxListToDel = []
    for idx, i in enumerate(crossLine):
        if popNum in i:
            if i[0] == popNum and not isVirusedComputer[i[1]]:
                virusedComputerN += 1
                nodeToBeCheck.append(i[1])
                isVirusedComputer[i[1]] = True
            elif i[1] == popNum and not isVirusedComputer[i[0]]:
                virusedComputerN += 1
                nodeToBeCheck.append(i[0])
                isVirusedComputer[i[0]] = True
            idxListToDel.append(idx)
    for i in sorted(idxListToDel, reverse=True):
        del crossLine[i]
            
print(virusedComputerN)