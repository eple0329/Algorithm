N, c, r = map(int, input().split())

LENGTH_N = 2 ** N
data = 0
def solve_square(length, r, c):
    global data
    if length == 1:
        return
    if r < length//2 and c < length//2:
        data += 0
        solve_square(length//2, r, c)
    elif r >= length//2 and c < length//2:
        data += (length//2) ** 2
        solve_square(length//2, r-(length//2), c)
    elif r < length//2 and c >= length//2:
        data += ((length//2) ** 2) * 2
        solve_square(length//2, r, c-(length//2))
    else:
        data += ((length//2) ** 2) * 3
        solve_square(length//2, r-(length//2), c-(length//2))
        
solve_square(LENGTH_N, r, c)
print(data)
