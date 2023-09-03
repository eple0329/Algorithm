def solution(number, limit, power):
    data = [0 for i in range(number+1)]
    answer = 0
    for i in range(1, number+1):
        for j in range(1, number//i+1):
            data[i*j] += 1
    for i in range(1, number+1):
        if data[i] <= limit:
            answer += data[i]
        else:
            answer += power
    return answer