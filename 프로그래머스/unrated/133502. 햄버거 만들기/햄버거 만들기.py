def solution(ingredient):
    answer = 0
    data = ingredient
    minus = 0
    for i in range(len(data)-3):
        if data[i-minus:i-minus+4] == [1, 2, 3, 1]:
            del(data[i-minus:i-minus+4])
            minus += 4
            answer += 1
    return answer