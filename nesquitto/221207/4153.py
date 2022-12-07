import sys

while True:
    math = list(map(int, sys.stdin.readline().split()))
    if math == [0,0,0]:
        break;
    else:
        math.sort()
        if math[2]**2 == math[1]**2 + math[0]**2:
            print('right')
        else:
            print('wrong')
