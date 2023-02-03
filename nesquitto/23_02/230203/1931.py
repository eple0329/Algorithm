import sys

N = int(sys.stdin.readline().rstrip())
MEETING_TIME = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]
END_MEETING_TIME = sorted(MEETING_TIME, key = lambda x:(x[1], x[0]))

use_time = 0
max_num_meeting_time = 0
for i in END_MEETING_TIME:
    if i[0] >= use_time:
        use_time = i[1]
        max_num_meeting_time += 1
print(max_num_meeting_time)