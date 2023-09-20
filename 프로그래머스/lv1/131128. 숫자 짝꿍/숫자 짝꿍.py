def solution(X, Y):
    answer = ''
    xArr = [0 for i in range(10)]
    yArr = [0 for i in range(10)]
    for i in X:
        xArr[int(i)] += 1
    for i in Y:
        yArr[int(i)] += 1

    for i in range(9, -1, -1):
        answer += str(i) * min(xArr[i], yArr[i])
    if answer == "":
        answer = "-1"
    if answer[0] == "0":
        answer = "0"
    return answer