from collections import deque
N = int(input())

SEA_MAP = [list(map(int, input().split())) for i in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

size_of_shark = 2
location_of_shark = (0, 0)
queue = deque()
for i in range(N):
    for j in range(N):
        if SEA_MAP[i][j] == 9:
            location_of_shark = (i, j)
SEA_MAP[location_of_shark[0]][location_of_shark[1]] = 0


time_to_solve = 0
is_eat_fish = True
num_eat_fish = 0

while is_eat_fish:
    if num_eat_fish == size_of_shark:
        num_eat_fish = 0
        size_of_shark += 1
    distance_map = [[-1 for i in range(N)] for j in range(N)]
    distance_map[location_of_shark[0]][location_of_shark[1]] = 0
    tmp_distance = 10000
    queue.clear()
    queue.append(location_of_shark)
    is_eat_fish = False
    while queue:
        location_now_x, location_now_y = queue.popleft()
        distance = distance_map[location_now_x][location_now_y]
        if tmp_distance != 10000 and distance > tmp_distance:
            continue
        for i in range(4):
            location_next_x = location_now_x + dx[i]
            location_next_y = location_now_y + dy[i]
            if 0 <= location_next_x < N and 0 <= location_next_y < N and distance_map[location_next_x][location_next_y] == -1:
                following = SEA_MAP[location_next_x][location_next_y]
                if  following <= size_of_shark:
                    if 0 < following < size_of_shark:
                        if tmp_distance == 10000:
                            tmp_distance = distance + 1
                        is_eat_fish = True
                        distance_map[location_next_x][location_next_y] = distance + 1
                    else:
                        distance_map[location_next_x][location_next_y] = distance + 1
                        queue.append((location_next_x, location_next_y))
    if tmp_distance != 10000:
        check = False
        for i in range(N):
            for j in range(N):
                if distance_map[i][j] == tmp_distance and 0 < SEA_MAP[i][j] < size_of_shark:
                    SEA_MAP[i][j] = 0
                    location_of_shark = (i, j)
                    check = True
                    break
            if check:
                break
        time_to_solve += tmp_distance
        num_eat_fish += 1
    if not is_eat_fish:
        print(time_to_solve)
        break


