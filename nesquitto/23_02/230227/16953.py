from collections import deque

A, B = map(int, input().split())

is_used = dict()
is_used[A] = 1
is_can = False
queue = deque()
queue.append(A)
while queue:
    now_num = queue.popleft()
    count = 0
    if now_num in is_used.keys():
        count = is_used[now_num]
    if count == 0:
        continue
    num_add_right = int(str(now_num) + '1')
    num_product = now_num * 2

    if  num_add_right <= B:
        if num_add_right == B:
            print(count+1)
            is_can = True
            break
        else:
            queue.append(num_add_right)
            is_used[num_add_right] = count+1
    if  num_product <= B:
        if num_product == B:
            is_can = True
            print(count+1)
            break
        else:
            queue.append(num_product)
            is_used[num_product] = count+1
if not is_can:
    print(-1)