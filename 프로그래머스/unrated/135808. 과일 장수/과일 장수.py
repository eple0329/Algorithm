def solution(k, m, score):
    sort_score = sorted(score)
    answer = 0
    while len(sort_score) >= m:
        tmp = 1
        a = -1
        for i in range(m):
            a = sort_score.pop()
        tmp *= m * a
        answer += tmp
    
    return answer