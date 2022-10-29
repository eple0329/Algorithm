N = int(input())
peopleList = []

for i in range(N):
    x, y = map(int, input().split())
    peopleList.append(( x, y))
for i in peopleList:
    rank = 0
    for j in peopleList:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank+1)