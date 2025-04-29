n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
point = [0, 0]
axis = dict()
axis['N'] = (0, 1)
axis['S'] = (0, -1)
axis['E'] = (1, 0)
axis['W'] = (-1, 0)

for direction, distance in moves:
    point[0] += axis[direction][0] * int(distance)
    point[1] += axis[direction][1] * int(distance)

print(point[0], point[1])

