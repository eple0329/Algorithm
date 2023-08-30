def solution(s):
    alphabet = [-1 for i in range(26)]
    answer = []
    for idx, i in enumerate(s):
        if alphabet[ord(i)-97] == -1:
            answer.append(-1)
            alphabet[ord(i)-97] = idx
        else:
            answer.append(idx - alphabet[ord(i)-97])
            alphabet[ord(i)-97] = idx
    return answer