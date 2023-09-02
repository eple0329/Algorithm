def solution(k, score):
    answer = []
    data = []
    for i in score:
        data.append(i)
        data.sort(reverse=True)
        if len(data) < k:
            answer.append(data[len(data)-1])
        else:
            answer.append(data[k-1])
    return answer