import sys
from collections import deque

for _ in range(int(sys.stdin.readline().rstrip())):
    A, B = map(int, sys.stdin.readline().split())
    
    resister_num = ['-' for i in range(10000)]
    queue = deque()
    queue.append(A)
    resister_num[A] = ''
    while queue:
        now_num = queue.popleft()
        now_num_D = (now_num * 2) % 10000
        now_num_S = (now_num - 1) if now_num != 0 else 9999
        string_now_num = '0' * (4-len(str(now_num))) + str(now_num)
        now_num_L = int(str(string_now_num)[1:] + str(string_now_num)[:1])
        now_num_R = int(str(string_now_num)[-1:] + str(string_now_num)[:-1])
        if resister_num[now_num_D] == '-':
            resister_num[now_num_D] = resister_num[now_num] + 'D'
            queue.append(now_num_D)
            if now_num_D == B:
                print(resister_num[now_num_D])
                break
        if resister_num[now_num_S] == '-':
            resister_num[now_num_S] = resister_num[now_num] + 'S'
            queue.append(now_num_S)
            if now_num_S == B:
                print(resister_num[now_num_S])
                break
        if resister_num[now_num_L] == '-':
            resister_num[now_num_L] = resister_num[now_num] + 'L'
            queue.append(now_num_L)
            if now_num_L == B:
                print(resister_num[now_num_L])
                break
        if resister_num[now_num_R] == '-':
            resister_num[now_num_R] = resister_num[now_num] + 'R'
            queue.append(now_num_R)
            if now_num_R == B:
                print(resister_num[now_num_R])
                break