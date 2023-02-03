N = int(input())
VIDEO_PIXEL = [list(input()) for i in range(N)]
print_str = ""
def solve(start_x, start_y, length):
    global print_str
    print_str += "("
    check_x = [start_x, start_x, start_x + length//2, start_x + length//2] # 0, 4, 0, 4
    check_y = [start_y, start_y + length//2, start_y, start_y + length//2] # 0, 0, 4, 4
    for i in range(4):
        tmp = VIDEO_PIXEL[check_x[i]][check_y[i]]
        is_zipped = True
        for j in range(check_x[i], check_x[i] + length//2):
            for k in range(check_y[i], check_y[i] + length//2):
                if tmp != VIDEO_PIXEL[j][k]:
                    is_zipped = False
                    break
            if not is_zipped:
                break
        if is_zipped:
            print_str += tmp
        else:
            solve(check_x[i], check_y[i], length//2)
    print_str += ")"

tmp = VIDEO_PIXEL[0][0]
is_zipped = True
for i in range(N):
    for j in range(N):
        if tmp != VIDEO_PIXEL[i][j]:
            is_zipped = False
            break
    if not is_zipped:
        break
if is_zipped:
    print(tmp)
else:
    solve(0, 0, N)
    print(print_str)
