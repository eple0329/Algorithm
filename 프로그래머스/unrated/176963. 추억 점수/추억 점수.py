def solution(name, yearning, photo):
    namedict = dict()
    for i in range(len(name)):
        namedict[name[i]] = yearning[i]
    answer = []
    for i in photo:
        tmp = 0
        for j in i:
            if j in namedict.keys():
                tmp += namedict[j]
        answer.append(tmp)
    return answer