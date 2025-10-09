from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

def DFS(arr, visited, v):
    visited[v] = True
    print(v, end = ' ')
    for i in range(1, n+1):
        if arr[v][i] == 1 and not visited[i]:
            DFS(arr, visited, i)


def BFS(arr, visited, v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
                if arr[v][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

visited = [False] * (n+1)
DFS(arr, visited, v)
print()
visited = [False] * (n+1)
BFS(arr, visited, v)