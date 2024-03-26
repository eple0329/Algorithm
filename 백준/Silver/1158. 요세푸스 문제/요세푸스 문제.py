import sys

N, K = map(int, sys.stdin.readline().split())

num_list = [i for i in range(N+1)]
return_list = []

idx = 0

while(N != 0):
    idx = (idx + K) % N
    if(idx == 0):
        idx = N
    return_list.append(num_list.pop(idx))
    N -= 1
    idx -= 1

print("<" + ", ".join(map(str, return_list)) + ">")