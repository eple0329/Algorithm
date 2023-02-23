from collections import deque

N, M = map(int, input().split())

game_map = [0 for i in range(101)]
game_map_visited = [False for i in range(101)]
ladder = [list(map(int, input().split())) for i in range(N)]
snake = [list(map(int, input().split())) for i in range(M)]

def check_move(num):
    final_num = num
    can_move = True
    while can_move:
        can_move = False
        for i in ladder:
            if i[0] == final_num:
                final_num = i[1]
                can_move = True
        for i in snake:
            if i[0] == final_num:
                final_num = i[1]
                can_move = True
    return final_num

queue = deque()
game_map[1] = 0
game_map_visited[1] = True
destination = check_move(1)
game_map[destination] = 0
game_map_visited[destination] = True
queue.append(destination)

goal = False
while queue:
    #print(queue)
    now_num = queue.popleft()
    count = game_map[now_num]
    for i in range(1, 7):
        next_destination = check_move(now_num + i)
        if now_num + i <= 100 and game_map_visited[next_destination] == False:
            game_map_visited[now_num + i] = True
            game_map_visited[next_destination] = True
            game_map[next_destination] = count + 1
            queue.append(next_destination)
            if next_destination == 100:
                goal = True
                break
    if goal:
        break
print(game_map[100])