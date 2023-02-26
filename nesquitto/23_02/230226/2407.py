N, M = map(int, input().split())

def factorial(n):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
    return tmp

print(factorial(N) // (factorial(N-M) * factorial(M)))