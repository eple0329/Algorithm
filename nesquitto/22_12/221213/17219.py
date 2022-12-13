import sys

M, N = map(int, sys.stdin.readline().split())

link = dict()

for i in range(M):
    url, pwd = sys.stdin.readline().split()
    link[url] = pwd
for i in range(N):
    src = sys.stdin.readline().rstrip()
    print(link[src])