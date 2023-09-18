def solution(a, b, n):
    answer = 0
    tmp = n
    print("now cola: " + str(n))
    while(True):
        c = tmp//a
        print("몫: " + str(c))
        tmp -= c * a
        print("뺀거: " + str(c*a))
        tmp += b * c
        print("더한거: " + str(b * c))
        print(tmp)
        answer += b * c
        print("answer: " + str(answer))
        if tmp < a:
            break
    return answer