A, B, V = map(int, input().split())
res = (V-A)//(A-B) + 1
if (V-A)%(A-B) !=0:
    res += 1
print(res)