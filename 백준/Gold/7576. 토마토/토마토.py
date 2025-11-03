import sys
from collections import Counter, deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m, n = map(int, sys.stdin.readline().split())

arr = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)

queue = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            queue.append((i, j, 0))
            visited[i][j] = True

while queue:
    currx, curry, day = queue.popleft()
    for d in range(4):
        nx = currx + dx[d]
        ny = curry + dy[d]
        if (nx >= 0 and nx < n and ny >= 0 and ny < m and 
            arr[nx][ny] == 0 and not visited[nx][ny]):
            queue.append((nx, ny, day+1))
            arr[nx][ny] = 1
            visited[nx][ny] = True
    

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            day = -1
            break

print(day)