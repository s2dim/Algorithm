import sys
from collections import deque
import heapq

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, k = map(int, sys.stdin.readline().split())

arr = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)

s, x, y = map(int, sys.stdin.readline().split())

t = 0
cnt = 0

queue = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] != 0:
            heapq.heappush(queue, (arr[i][j], i, j))
            visited[i][j] = True
            cnt += 1

while t != s:
    if cnt == n*n:
        break

    temp = []
    while queue:
        virus, currx, curry = heapq.heappop(queue)

        for d in range(4):
            nx = currx + dx[d]
            ny = curry + dy[d]

            if (nx >= 0 and nx < n and ny >= 0 and ny < n and
                arr[nx][ny] == 0 and not visited[nx][ny]):
                arr[nx][ny] = virus
                heapq.heappush(temp, (arr[nx][ny], nx, ny))
                visited[nx][ny] = True
                cnt += 1

    queue = temp
    t += 1

print(arr[x-1][y-1])




