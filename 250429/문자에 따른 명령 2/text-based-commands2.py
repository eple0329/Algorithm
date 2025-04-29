dirs = input()

# Please write your code here.
axis = [(1,0), (0, 1), (-1, 0), (0, -1)]
direction = 1
point = [0, 0]
for string in dirs:
    if string == 'L':
        direction = (direction + 1) % 4
    if string == 'R':
        direction = (4 + direction - 1) % 4
    if string == 'F':
        point[0] += axis[direction][0]
        point[1] += axis[direction][1]

print(point[0], point[1])