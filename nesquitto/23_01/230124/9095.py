T = int(input())

# 규칙찾기 문제

n = [1, 2, 4]
for i in range(8):
    n.append(n[-1]+n[-2]+n[-3])
for _ in range(T):
    print(n[int(input())-1])