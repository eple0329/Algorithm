UDPC_input = list(input())
U_score = 0
D_score = 0
P_score = 0
C_score = 0
is_winner = False
for i in UDPC_input:
    if i == "U":
        U_score += 1
    elif i == "D":
        D_score += 1
    elif i == "P":
        P_score += 1
    else:
        C_score += 1

mid_DP_score = D_score + P_score
if mid_DP_score % 2 == 1:
    mid_DP_score //=2
    mid_DP_score += 1
else:
    mid_DP_score //=2
if U_score+C_score > mid_DP_score:
    print("U", end="")
    is_winner = True
if D_score + P_score > 0:
    print("DP", end="")
    is_winner = True
if not is_winner:
    print("C", end="")
