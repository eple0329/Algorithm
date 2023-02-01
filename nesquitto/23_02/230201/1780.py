import sys

N = int(sys.stdin.readline())

PAPER_DATA  = []

for i in range(N):
    PAPER_DATA.append(list(map(int, sys.stdin.readline().split())))

result_value = [0, 0, 0]

def solve_recurrence(start_idx_x, start_idx_y, length):
    global result_value
    
    is_unify = True
    first_value = PAPER_DATA[start_idx_x][start_idx_y]
    for i in range(start_idx_x, start_idx_x + length):
        for j in range(start_idx_y, start_idx_y + length):
            if PAPER_DATA[i][j] != first_value:
                is_unify = False
                break
        if not is_unify:
            break
    if is_unify:
        result_value[first_value] += 1

    else:
        next_length = length//3
        solve_recurrence(start_idx_x, start_idx_y, next_length)
        solve_recurrence(start_idx_x + next_length, start_idx_y, next_length)
        solve_recurrence(start_idx_x + next_length * 2, start_idx_y, next_length)
        solve_recurrence(start_idx_x, start_idx_y + next_length, next_length)
        solve_recurrence(start_idx_x + next_length, start_idx_y + next_length, next_length)
        solve_recurrence(start_idx_x + next_length * 2, start_idx_y + next_length, next_length)
        solve_recurrence(start_idx_x, start_idx_y + next_length * 2, next_length)
        solve_recurrence(start_idx_x + next_length, start_idx_y + next_length * 2, next_length)
        solve_recurrence(start_idx_x + next_length * 2, start_idx_y + next_length * 2, next_length)
        return

solve_recurrence(0, 0, N)
print(result_value[-1])
print(result_value[0])
print(result_value[1])

'''
    13~25줄
    global num_zero_paper
    global num_minus_paper
    global num_plus_paper
    is_minus = True
    is_zero = True
    is_plus = True
    for i in range(start_idx_x, start_idx_x + length):
        for j in range(start_idx_y, start_idx_y + length):
            if PAPER_DATA[i][j] == -1:
                is_zero = False
                is_plus = False
            elif PAPER_DATA[i][j] == 0:
                is_minus = False
                is_plus = False
            else:
                is_minus = False
                is_zero = False
        if not is_zero and not is_minus and not is_plus:
            break
    if is_zero:
        num_zero_paper += 1
        return
    elif is_minus:
        num_minus_paper += 1
        return
    elif is_plus:
        num_plus_paper += 1
        return
'''