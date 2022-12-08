N = int(input())
axis = []
for _ in range(N):
    axis.append(tuple(map(int, input().split())))
axis = sorted(axis, key=lambda l:(l[1], l[0]))
for i in axis:
    print(i[0], i[1])