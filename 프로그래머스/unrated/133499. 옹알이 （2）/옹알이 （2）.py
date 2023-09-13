def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        start = 0
        before = ""
        while(True):
            end = start
            for j in word:
                if j != before:
                    if len(j) <= len(i[start:]):
                        if i[start:start+len(j)] == j:
                            start += len(j)
                            before = j
                            break
            if end == start:
                break
            if start >= len(i):
                answer += 1
                break
    return answer