
import sys
from collections import deque
sys.setrecursionlimit(10000)

n, m, v = map(int, sys.stdin.readline().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]

# 배열 추가
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

queue = []


def DFS(v):
    stack = [v]
    ans = []

    while stack:
        a = stack.pop()
        if not visited[a]:
            visited[a] = True
            ans.append(str(a))

        for i in range(n, 0, -1):
            if arr[a][i] == 1 and not visited[i]:
                stack.append(i)

    print(' '.join(ans))


def BFS(v):
    queue = deque()
    queue.append(v)
    ans = []

    while queue:
        a = queue.popleft()
        for i in range (1, n + 1):
            if arr[a][i] == 1 and not visited[i]:
                queue.append(i)

        if not visited[a]:
            visited[a] = True
            ans.append(str(a))

    print(' '.join(ans))


visited = [False] * (n + 1)
DFS(v)

visited = [False] * (n + 1)
BFS(v)
