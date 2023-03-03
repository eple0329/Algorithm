import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

bus_info = [[] for i in range(N+1)]
for i in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    bus_info[start].append((end, cost)) # start에서 end로 갈 때의 cost

start, end = map(int, sys.stdin.readline().split()) # start에서 end로 가기를 원함
cost_to_end = [1000000000 for i in range(N+1)] # start에서 각 지점에 갈 때의 최소비용(갱신용)
cost_to_end[start] = 0 # 시작하는 곳은 0으로 시작

stack = []
for i in bus_info[start]: # 처음 시작지점에서 갈 수 있는 곳과 비용
    end, cost = i
    stack.append((start, end, cost)) # 해당 비용을 내고 도착점까지 감
while stack:
    pop_start, pop_end, pop_cost = stack.pop()
    if cost_to_end[pop_start] + pop_cost < cost_to_end[pop_end]:
        cost_to_end[pop_end] = cost_to_end[pop_start] + pop_cost
    else:
        continue
    for i in bus_info[pop_end]:
        info_end, info_cost = i
        stack.append((pop_end, info_end, info_cost))

print(cost_to_end[end])