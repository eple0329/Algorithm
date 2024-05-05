N = int(input())

switch_status = [-1]

switch_status += list(map(int, input().split()))

def change_status(num):
    if switch_status[num] == 0:
        switch_status[num] = 1
    else:
        switch_status[num] = 0

M = int(input())
for _ in range(M):
    gender, switch_num = map(int, input().split())
    if gender == 1: # 남학생
        for j in range(switch_num, N+1, switch_num):
            change_status(j)
        
    else: # 여학생
        change_status(switch_num)
        for i in range(1, N//2):
            if switch_num - i <= 0 or switch_num + i >= N+1:
                break
            if switch_status[switch_num - i] == switch_status[switch_num + i]:
                change_status(switch_num - i)
                change_status(switch_num + i)
            else:
                break
            
for i in range(1, N+1):
    print(switch_status[i], end=' ')
    if(i % 20 == 0):
        print()