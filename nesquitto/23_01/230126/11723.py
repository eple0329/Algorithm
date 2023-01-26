import sys
M = int(input())
dataSet = set()
for i in range(M):
    command = list(sys.stdin.readline().split())
    if command[0] == 'add':
        dataSet.add(int(command[1]))
    elif command[0] == 'remove':
        if int(command[1]) in dataSet:
            dataSet.remove(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in dataSet:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in dataSet:
            dataSet.remove(int(command[1]))
        else:
            dataSet.add(int(command[1]))
    elif command[0] == 'all':
        dataSet = {i for i in range(1, 21)}
    elif command[0] == 'empty':
        dataSet.clear()
    else:
        pass