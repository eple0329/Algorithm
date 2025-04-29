n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c) # r = y, c = x

# Please write your code here.

point = [c, r]
axis = dict()
axis['U'] = [0, 1]
axis['D'] = [0, -1]
axis['R'] = [1, 0]
axis['L'] = [-1, 0]
reverse = dict()
reverse['U'] = 'D'
reverse['D'] = 'U'
reverse['R'] = 'L'
reverse['L'] = 'R'

direction = d

for i in range(t):
    dx, dy = axis[direction]
    if 1 <= point[0] + dx <= n and 1 <= point[1] + dy <= n:
        point[0] += dx
        point[1] += dy
    else:
        direction = reverse[direction]

print(point[1], point[0])
