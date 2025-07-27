
import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

def DFS(v):
    visited[v] = True
    for i in range(1, n + 1):
        if not visited[i] and arr[v][i] == 1:
            DFS(i)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
