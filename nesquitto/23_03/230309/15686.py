import sys
from itertools import combinations

input = sys.stdin.readline

def calc_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def chicken_distance(chicken, house):
    tmp = 10000
    for i in chicken:
        tmp = min(tmp, calc_distance(i, house))
    return tmp
        

N, M = map(int, input().split())

city_map = [list(map(int, input().split())) for i in range(N)]
chicken_location = []
house_location = []
for i in range(N):
    for j in range(N):
        if city_map[i][j] == 2:
            chicken_location.append((i, j))
        elif city_map[i][j] == 1:
            house_location.append((i, j))

min_chicken_distance = 10000000
for chicken_choice in list(combinations(chicken_location, M)):
    tmp_chicken_distance = 0
    for house in house_location:
        tmp_chicken_distance += chicken_distance(chicken_choice, house)
    min_chicken_distance = min(min_chicken_distance, tmp_chicken_distance)

print(min_chicken_distance)
