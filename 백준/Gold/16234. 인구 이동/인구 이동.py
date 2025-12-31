import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, l, r = map(int, sys.stdin.readline().split())

arr = []

# 배열 생성
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)


day = 0

while True:
    visited = [[False] * (n) for _ in range(n)]
    state = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue = deque([(i, j, arr[i][j])])
                visited[i][j] = True
                cnt = arr[i][j]
                state += 1

                temp = []
                while queue:
                    currx, curry, people = queue.popleft()
                    temp.append([currx, curry])

                    for d in range(4):
                        nx = currx + dx[d]
                        ny = curry + dy[d]

                        if (nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny] and
                            abs(arr[nx][ny] - people) >= l and abs(arr[nx][ny] - people) <= r):
                            queue.append((nx, ny, arr[nx][ny]))
                            cnt += arr[nx][ny]
                            visited[nx][ny] = True

                many = cnt // len(temp)
                for x, y in temp:
                    arr[x][y] = many

            

    if state == n*n:
        break
    else:
        day += 1

print(day)