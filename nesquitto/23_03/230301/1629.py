A, B, C = map(int, input().split())
storage = dict()

def solve(N):
    global A, C, storage
    if N in storage.keys():
        return storage[N]
    if N == 1:
        return A % C
    elif N == 2:
        return A * A % C
    else:
        data = (solve(N//2) * solve(N//2 + N%2)) % C
        storage[N] = data
        return data

print(solve(B) % C)