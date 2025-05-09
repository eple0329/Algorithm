n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
total_count = 0

def is_happy(num_list, m):
    tmp = 1
    if len(num_list) == 1 and m == 1:
        return True
    for i in range(1, len(num_list)):
        if num_list[i] == num_list[i-1]:
            tmp += 1
        else:
            tmp = 1

        if tmp >= m:
            return True
    return False
        
for i in grid:
    if is_happy(i, m):
        total_count += 1
for i in zip(*grid):
    if is_happy(i, m):
        total_count += 1

print(total_count)