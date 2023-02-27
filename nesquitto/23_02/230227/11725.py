import sys

N = int(sys.stdin.readline().rstrip())

NODE_TO_NODE = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    NODE_TO_NODE[a].append(b)
    NODE_TO_NODE[b].append(a)


parent_of_n = [0 for i in range(N+1)]

stack = [1]

while stack:
    now_node = stack.pop()
    for i in NODE_TO_NODE[now_node]:
        if parent_of_n[i] == 0:
            parent_of_n[i] = now_node
            stack.append(i)
        else:
            continue
for i in range(2, len(parent_of_n)):
    print(parent_of_n[i])