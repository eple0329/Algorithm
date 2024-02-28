import sys

def input():
    return sys.stdin.readline().rstrip()

student = [0 for i in range(31)]

for i in range(28):
    student[int(input())] = 1

for i in range(1, 31):
    if student[i] == 0:
        print(i)
