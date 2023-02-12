N = int(input())
M = int(input())
S = input()

pn_list = []
count = 0
for i in range(M):
    if count != 0:
        count -= 1
        continue
    if S[i] == "I":
        count = 0
        for j in range(i+1, M):
            if i % 2 == 1:
                if j % 2 == 1:
                    if S[j] == "I":
                        count += 1
                    else:
                        break
                else:
                    if S[j] == "O":
                        count += 1
                    else:
                        break
            else:
                if j % 2 == 0:
                    if S[j] == "I":
                        count += 1
                    else:
                        break
                else:
                    if S[j] == "O":
                        count += 1
                    else:
                        break
        if count >= 2:
            pn_list.append(count//2)
        else:
            count = 0

pn_count = 0
for i in pn_list:
    if N <= i:
        pn_count += i-N+1
print(pn_count)