from collections import deque
import sys

data = deque()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        data.append(command[1])
    elif command[0] == 'pop':
        if len(data) == 0:
            print(-1)
        else:
            print(data.popleft())
    elif command[0] == 'size':
        print(len(data))
    elif command[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
    elif command[0] == 'back':
        if len(data) == 0:
            print(-1)
        else:
            print(data[len(data)-1])
    else:
        pass
