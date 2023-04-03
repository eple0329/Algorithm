A = int(input())
cycle = 0
tmp = A
while True:
    cycle += 1
    if tmp < 10:
        str_tmp = "0" + str(tmp)
    else:
        str_tmp = str(tmp)
    add_num = int(str_tmp[0]) + int(str_tmp[1])
    tmp = int(str_tmp[1] + str(add_num%10))
    if int(tmp) == A:
        print(cycle)
        break
    
    
    