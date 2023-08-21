def solution(players, callings):
    racing = dict()
    bottom = ""
    for i in range(len(players)):
        if i == 0:
            racing[players[i]] = [i+1, "FIRST", players[i+1]]
        elif i == len(players)-1:
            racing[players[i]] = [i+1, players[i-1], "BOTTOM"]
        else:
            racing[players[i]] = [i+1, players[i-1], players[i+1]]
            
    for i in callings:
        front = racing[i][1]
        back = racing[i][2]
        caller = i
        if racing[front][1] != "FIRST":
            racing[racing[front][1]] = [racing[racing[front][1]][0],racing[racing[front][1]][1],caller]
        if back != "BOTTOM":
            racing[back] = [racing[back][0], front, racing[back][2]]
        racing[caller] = [racing[front][0], racing[front][1], front]
        racing[front] = [racing[front][0]+1, caller, back]

    top = ""
    award = []
    for i in racing.keys():
        if racing[i][1] == "FIRST":
            top = i
            break
    award.append(top)
    
    for i in range(len(players)-1):
        top = racing[top][2]
        award.append(top)
        if top == "BOTTOM":
            break
    
    
    answer = list(award)
    return answer