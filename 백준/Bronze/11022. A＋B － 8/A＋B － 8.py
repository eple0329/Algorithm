import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print("Case #" + str(i+1) + ": " + str(A) + " + " + str(B) + " = " + str(A+B))