N = int(input())

empty_num = [False for i in range(N+1)]
empty_num[0], empty_num[1] = True, True
false_num_list = []

mid_idx = N//2
mid = N//2 + 1
max_num = N


while True:
    print("? " + str(mid), flush=True)
    answer = int(input())
    if answer == 1:
        for i in range(2, mid+1):
            if empty_num[i] == False:
                for j in range(1, max_num//i + 1):
                    empty_num[i * j] = True
        false_num_list.clear()
        for idx in range(max_num+1):
            if empty_num[idx] == False:
                false_num_list.append(idx)
        mid_idx = len(false_num_list)//2
        mid = false_num_list[mid_idx]
    else:
        max_num = mid
        if mid_idx == 0:
            print('! ' + str(false_num_list[0]), flush=True)
            break
        if false_num_list == []:
            false_num_list = list(range(2, max_num+1))
            mid_idx = len(false_num_list)//2
            mid = false_num_list[mid_idx]
        else:
            mid_idx = mid_idx//2
            mid = false_num_list[mid_idx]
    if len(false_num_list) == 1:
            print('! ' + str(false_num_list[0]), flush=True)
            break