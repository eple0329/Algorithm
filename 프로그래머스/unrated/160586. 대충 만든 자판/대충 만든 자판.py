def solution(keymap, targets):
    dic = dict()
    for i in keymap:
        for j in range(len(i)):
            if i[j] in dic.keys():
                dic[i[j]] = min(dic[i[j]], j+1)
            else:
                dic[i[j]] = j+1
    answer = []
    for i in targets:
        res = 0
        for j in i:
            if j in dic.keys():
                res += dic[j]
            else:
                res = -1
                break
        answer.append(res)

    
    return answer