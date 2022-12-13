x, y, w, h = map(int, input().split())
a, b, c, d = x, y, w-x, h-y
print(min([a, b, c, d]))