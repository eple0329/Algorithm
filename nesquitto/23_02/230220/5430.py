import sys
from collections import deque

for T in range(int(sys.stdin.readline().rstrip())):
    P = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    array = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if N == 0:
        array = []
    is_reverse = False
    is_error = False
    for i in P:
        if i == 'R':
            if is_reverse:
                is_reverse = False
            else:
                is_reverse = True
        elif i == 'D':
            if len(array) <= 0:
                is_error = True
                break
            if is_reverse:
                array.pop()
            else:
                array.popleft()
        else:
            pass
    if is_error:
        print('error')
    else:
        print('[', end="")
        if is_reverse:
            array.reverse()
        print(','.join(array), end="")
        print(']')
            
    