def solution(wallpaper):
    y = len(wallpaper)
    x = len(wallpaper[0])
    min_y, min_x, max_y, max_x = 100, 100, 0, 0
    for i in range(y):
        for j in range(x):
            if wallpaper[i][j] == '#':
                if i < min_y:
                    min_y = i
                if j < min_x:
                    min_x = j
                if i > max_y:
                    max_y = i
                if j > max_x:
                    max_x = j

    answer = [min_y, min_x, max_y+1, max_x+1]
    return answer