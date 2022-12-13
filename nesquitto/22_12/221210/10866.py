from collections import deque
import sys

N = int(sys.stdin.readline())
dequeSpace = deque()

for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        dequeSpace.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        dequeSpace.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(dequeSpace) == 0:
            print(-1)
        else:
            print(dequeSpace.popleft())
    elif command[0] == 'pop_back':
        if len(dequeSpace) == 0:
            print(-1)
        else:
            print(dequeSpace.pop())
    elif command[0] == 'size':
        print(len(dequeSpace))
    elif command[0] == 'empty':
        if len(dequeSpace) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dequeSpace) == 0:
            print(-1)
        else:
            print(dequeSpace[0])
    elif command[0] == 'back':
        if len(dequeSpace) == 0:
            print(-1)
        else:
            print(dequeSpace[len(dequeSpace)-1])
    else:
        pass
