import sys
import math

M, N = map(int, sys.stdin.readline().split())
# M, N을 입력받음

num_list = [True for _ in range(N+1)]
# N+1개의 True로 된 배열을 선언

num_list[0] = False
num_list[1] = False
# 0, 1은 소수가 아님

for i in range(2, math.floor(math.sqrt(N))+1):
    if num_list[i] == False:
        continue
    for j in range(i * 2, N+1, i):
        num_list[j] = False
for i in range(M, N+1):
    if num_list[i]:
        print(i)