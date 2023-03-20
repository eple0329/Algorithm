N = int(input())
count_zero = 0
count_first = 1
tmp = 0

for i in range(N-1):
    tmp = count_zero
    count_zero += count_first
    count_first = tmp
if N == 1:
    print(1)
else:
    print(count_first + count_zero)
