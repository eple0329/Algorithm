from collections import deque
import sys

stack = deque()
N = int(input())
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(stack) !=0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) !=0:
            print(stack[len(stack)-1])
        else:
            print(-1)
