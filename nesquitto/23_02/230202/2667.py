N = int(input())
apartment_data_list = [list(map(int, list(input()))) for i in range(N)]

DIFFERENCE_X = (0, 0, 1, -1)
DIFFERENCE_Y = (1, -1, 0, 0)

total_apartment_num_list = []

for i in range(N):
    for j in range(N):
        if apartment_data_list[i][j] == 1:
            stack = [(i, j)]
            apartment_num = 0
            while stack:
                now_x, now_y = stack.pop()
                if apartment_data_list[now_x][now_y] != 1:
                    continue
                apartment_data_list[now_x][now_y] = 2
                apartment_num += 1
                for k in range(4):
                    next_x, next_y = now_x + DIFFERENCE_X[k], now_y + DIFFERENCE_Y[k]
                    if 0 <= next_x < N and 0 <= next_y < N and apartment_data_list[next_x][next_y] == 1:
                        stack.append((next_x, next_y))
            total_apartment_num_list.append(apartment_num)

print(len(total_apartment_num_list))

for i in sorted(total_apartment_num_list):
    print(i)