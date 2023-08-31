from collections import deque

def solution(s):
    answer = 0
    data = deque(s)
    crit = ""
    tmp = [0, 0]
    while data:
        tmpdata = data.popleft()
        #print(tmpdata)
        if crit == "":
            crit = tmpdata
            #print(1)
        if tmpdata == crit:
            tmp[0] += 1
            #print(2)
        else:
            tmp[1] += 1
            #print(3)
        #print(tmp)
        if tmp[0] != 0 and tmp[1] != 0 and tmp[0] == tmp[1]:
            answer += 1
            crit = ""
            tmp = [0, 0]
            #print(4)
    if tmp != [0, 0]:
        answer += 1
    return answer