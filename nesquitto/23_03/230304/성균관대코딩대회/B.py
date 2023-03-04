S = input().rstrip()

DELIMITER_ONE_CHARACTER = ('<', '>', '(', ')', ' ')
DELIMITER_TWO_CHARACTER = ('&', '|')

token_and_delimiter = []
start_idx = 0
pass_one_time = False
for i in range(len(S)):
    if pass_one_time:
        pass_one_time = False
        continue
    tmp = S[i] # 현재 문자
    tmp1 = S[start_idx:i] # 자를 문자 (구분자 전까지)
    tmp2 = S[i:i+2] # 구분자가 2개일때
    if S[i] in DELIMITER_ONE_CHARACTER:
        token_and_delimiter.append(S[start_idx:i])
        if S[i] == ' ':
            pass
        else:
            token_and_delimiter.append(S[i])
        start_idx = i+1
    elif S[i] in DELIMITER_TWO_CHARACTER:
        token_and_delimiter.append(S[start_idx:i])
        token_and_delimiter.append(S[i:i+2])
        start_idx = i+2
        pass_one_time = True
    else:
        pass
token_and_delimiter.append(S[start_idx:])

for i in token_and_delimiter:
    if i == ' ' or i == '':
        pass
    else:
        print(i, end=' ')