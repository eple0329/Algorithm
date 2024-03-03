import sys

def input():
    return sys.stdin.readline().rstrip()

Q = int(input())

for _ in range(Q):
    TA, TB, VA, VB = map(int, input().split())
    
    totalB = TB * VB
    resultTime = totalB # B가 끝나는 시간
    if TA * VA <= totalB: 
        print(resultTime)
    else: # A가 B보다 늦게 끝날 때
        lastA = TA * VA - totalB
        resultTime += (lastA // TA // 2) * TA
        if lastA // TA % 2 != 0: # 남은 A를 둘이서 공평하게 나눌 수 없는 경우
            resultTime += TA
        elif lastA % TA != 0: # 나머지가 공평하게 나눠지는데, B가 다 끝났을 때 A랑 타이밍이 안맞는 경우
            resultTime += lastA % TA
        print(resultTime)