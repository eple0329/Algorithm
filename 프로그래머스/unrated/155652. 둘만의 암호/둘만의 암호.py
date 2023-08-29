def solution(s, skip, index):
    answer = []
    skip_num = []
    for i in skip:
        skip_num.append(ord(i))
    for i in s:
        n = 0
        num = ord(i)
        while(n < index):
            num += 1
            if num > ord("z"):
                num = ord("a")
            if num not in skip_num:
                n += 1
        answer.append(chr(num))
    return "".join(answer)