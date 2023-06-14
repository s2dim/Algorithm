import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

A = [[] for i in range(n+1)]

visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)