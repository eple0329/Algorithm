while True:
    sentence = input()
    if sentence == '.':
        break
    isBalanced = True
    tmp = []
    for _ in sentence:
        if _ == '[' or _ == '(':
            tmp.append(_)
        elif _ == ']':
            if len(tmp) > 0:
                if tmp.pop() == '[':
                    continue
                else:
                    isBalanced = False
                    break
            else:
                isBalanced = False
                break
        elif _ == ')':
            if len(tmp) > 0:
                if tmp.pop() == '(':
                    continue
                else:
                    isBalanced = False
                    break
            else:
                isBalanced = False
                break
    if len(tmp) != 0:
        isBalanced = False
    if isBalanced:
        print('yes')
    else:
        print('no')