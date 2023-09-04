def solution(food):
    answer = ''
    data = []
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            data.append(i)
    answer = ''.join(map(str, data))
    answer += '0'
    data.reverse()
    answer += ''.join(map(str, data))
    return answer