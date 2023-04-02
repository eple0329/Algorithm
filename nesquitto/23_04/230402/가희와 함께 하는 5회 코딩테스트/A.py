height = 0
for i in range(4):
    floor_data = list(input().split())
    if floor_data[0] == "Es":
        height += int(floor_data[1]) * 21
    else:
        height += int(floor_data[1]) * 17
print(height)