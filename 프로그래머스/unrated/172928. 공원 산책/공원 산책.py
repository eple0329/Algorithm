def solution(park, routes):
    x_len = len(park)
    y_len = len(park[0])
    start_xy = [-1, -1]
    for i in range(x_len):
        for j in range(y_len):
            if park[i][j] == 'S':
                start_xy = [i, j]
    #print(start_xy)
    for i in routes:
        direction, distance = i.split()
        distance = int(distance)
        if direction == "W":
            if 0 <= start_xy[1] - distance < y_len:
                is_obstacle = False
                for j in range(1, distance+1):
                    if park[start_xy[0]][start_xy[1]-j] == "X":
                        is_obstacle = True
                        break
                if not is_obstacle:
                    start_xy = [start_xy[0], start_xy[1]-distance]
                    #print("Move: " + direction + str(distance))
                    #print(start_xy)
        elif direction == "E":
            if 0 <= start_xy[1] + distance < y_len:
                is_obstacle = False
                for j in range(1, distance+1):
                    if park[start_xy[0]][start_xy[1]+j] == "X":
                        is_obstacle = True
                        break
                if not is_obstacle:
                    start_xy = [start_xy[0], start_xy[1]+distance]
                    #print("Move: " + direction + str(distance))
                    #print(start_xy)
        elif direction == "N":
            if 0 <= start_xy[0] - distance < x_len:
                is_obstacle = False
                for j in range(1, distance+1):
                    if park[start_xy[0]-j][start_xy[1]] == "X":
                        is_obstacle = True
                        break
                if not is_obstacle:
                    start_xy = [start_xy[0]-distance, start_xy[1]]
                    #print("Move: " + direction + str(distance))
                    #print(start_xy)
        elif direction == "S":
            if 0 <= start_xy[0] + distance < x_len:
                is_obstacle = False
                for j in range(1, distance+1):
                    if park[start_xy[0]+j][start_xy[1]] == "X":
                        is_obstacle = True
                        break
                if not is_obstacle:
                    start_xy = [start_xy[0]+distance, start_xy[1]]
                    #print("Move: " + direction + str(distance))
                    #print(start_xy)
        else:
            answer = ["Error"]
            break
    answer = start_xy
    return answer