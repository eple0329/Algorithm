time_score = [list(input().split()) for i in range(8)]
for i in range(8):
    time_score[i][0] = list(map(int, time_score[i][0].split(':')))

time_score.sort(key=lambda x:x[0])
blue_score = 0
red_score = 0
score = [10, 8, 6, 5, 4, 3, 2, 1, 0]
for i in range(8):
    if time_score[i][1] == 'B':
        blue_score += score[i]
    else:
        red_score += score[i]

if blue_score > red_score:
    print('Blue')
else:
    print('Red')