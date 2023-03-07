import sys

N = int(sys.stdin.readline().rstrip())

count = 0

def solve(solve_axis, row, x, y):
    is_ok = True
    for i in solve_axis:
        dx, dy = i
        if dy == y or x-dx == abs(y-dy):
            is_ok = False
            break
    if is_ok:
        if x == N-1:
            global count
            count += 1
            return
        solve_axis.append((x, y))
        row[y] = True
        for i in range(N):
            if row[i]:
                continue
            solve(solve_axis[:], row[:], x+1, i)
    

for i in range(N):
    solve([], [False for i in range(N)], 0, i)
print(count)