import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, sys.stdin.readline().split())

arr = []
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x = i
            y = j
            break


queue = deque([(x, y)])
visited[x][y] = 0

while queue:
    currx, curry = queue.popleft()

    for d in range(4):
        nx = dx[d] + currx
        ny = dy[d] + curry

        if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == 1 and visited[nx][ny] == -1:
            queue.append((nx, ny))
            visited[nx][ny] = visited[currx][curry] + 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            visited[i][j] = 0
        print(visited[i][j], end=' ')
    print()