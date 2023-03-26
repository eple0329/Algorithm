N = int(input())
D_score, P_score = 0, 0
is_end = False
for i in range(N):
    winner = input()
    if is_end:
        continue
    if winner == "D":
        D_score += 1
    else:
        P_score += 1
    if abs(D_score-P_score) >= 2:
        print(str(D_score) + ":" + str(P_score))
        is_end = True

if not is_end:
    print(str(D_score) + ":" + str(P_score))