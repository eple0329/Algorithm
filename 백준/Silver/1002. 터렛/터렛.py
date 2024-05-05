import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    distance_turret = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    if distance_turret == 0: # 같은 위치
        if r1 == r2: # 같은 거리 -> 반경이 모두 겹침
            print(-1)
        else: # 다른 거리 -> 한 원이 다른 원 내부에 존재
            print(0)
    else: # 다른 위치
        if r1 + r2 == distance_turret: # 터렛 사이 한점 만남
            print(1)
        elif abs(r1 - r2) == distance_turret: # 터렛 바깥쪽 한점 만남
            print(1)
        elif ((abs(r1 - r2) < distance_turret) and (distance_turret < r1 + r2)):
            print(2)
        else: # r1 + r2를 한 값이 distance보다 짧음 -> 만나지 않음
            print(0)