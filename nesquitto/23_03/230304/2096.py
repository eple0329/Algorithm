import sys

max_score = [0, 0, 0]
min_score = [0, 0, 0]
for i in range(int(sys.stdin.readline().rstrip())):
    tmp_min = list(map(int, input().split()))
    tmp_max = tmp_min[:]
    if i  == 0:
        max_score = tmp_min[:]
        min_score = tmp_max[:]
    else:
        tmp_max[0] += max(max_score[0], max_score[1])
        tmp_max[1] += max(max_score)
        tmp_max[2] += max(max_score[1], max_score[2])
        tmp_min[0] += min(min_score[0], min_score[1])
        tmp_min[1] += min(min_score)
        tmp_min[2] += min(min_score[1], min_score[2])
        max_score = tmp_max[:]
        min_score = tmp_min[:]
print(max(max_score), min(min_score))