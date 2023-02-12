import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    memoization_dict = dict()
    FIND_DIFFERENCE = x-y
    END_DIFFERENCE = M-N
    max_a, max_b, max_count = 1, 1, 1
    a, b = 1, 1
    count = 1
    is_end = False
    if END_DIFFERENCE in memoization_dict.keys():
        a, b, count = memoization_dict[END_DIFFERENCE][0], memoization_dict[END_DIFFERENCE][1], memoization_dict[END_DIFFERENCE][2]
        is_end = True
    elif FIND_DIFFERENCE in memoization_dict.keys():
        if is_end:
            if memoization_dict[END_DIFFERENCE][2] > memoization_dict[FIND_DIFFERENCE][2]:
                a, b, count = memoization_dict[FIND_DIFFERENCE][0], memoization_dict[FIND_DIFFERENCE][1], memoization_dict[FIND_DIFFERENCE][2]
    else:
        a, b, count = max_a, max_b, max_count
    
    while a-b != FIND_DIFFERENCE and a-b != END_DIFFERENCE:
        if M-a > N-b:
            plus_num = N-b+1
            count += plus_num
            a += plus_num
            b = 1
        elif M-a < N-b:
            plus_num = M-a+1
            count += plus_num
            b += plus_num
            a = 1
        else:
            break
        memoization_dict[a-b] = [a, b, count]
        max_a, max_b, max_count = a, b, count
    if a-b == FIND_DIFFERENCE:
        count += x - a
        print(count)
    else:
        print(-1)
