import sys

N = int(sys.stdin.readline().rstrip())

id_list = []
for _ in range(N):
    id_list.append(sys.stdin.readline().rstrip())

id_length = len(id_list[0])
min_length = 1
for i in range(id_length+1):
    tmp_list = []
    for j in id_list:
        #print(j[-i:])
        if j[-i:] in tmp_list:
            min_length += 1
            break
        else:
            tmp_list.append(j[-i:])
    if i == min_length:
        print(min_length)
        break