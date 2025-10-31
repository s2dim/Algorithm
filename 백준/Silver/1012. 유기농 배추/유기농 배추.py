from collections import deque

import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())

for t in range(T): 
    # 가로 m  - y 세로 n - x
    m, n, k = map(int, sys.stdin.readline().split())

    arr = [[0] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    visited = [[False] * m for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                cnt += 1
                while queue:
                    currx, curry = queue.popleft()

                    for d in range(4):
                        nx = currx + dx[d]
                        ny = curry + dy[d]

                        if (nx >= 0 and nx < n and ny >= 0 and ny < m and
                            arr[nx][ny] == 1 and not visited[nx][ny]):
                            visited[nx][ny] = True
                            queue.append((nx, ny))

    print(cnt)