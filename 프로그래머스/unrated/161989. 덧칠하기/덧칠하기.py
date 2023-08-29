def solution(n, m, section):
    data = [0 for i in range(n+1)]
    sum = 0
    for i in section:
        data[i] = 1
    for i in range(n+1):
        if data[i] == 1:
            sum+=1
            for j in range(m):
                if i+j<n+1:
                    data[i+j] = 0
    

    answer = sum
    return answer