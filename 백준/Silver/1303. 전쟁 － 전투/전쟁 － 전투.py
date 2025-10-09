from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split()) # m*n 행렬

arr = []
visited = [[False] * n for _ in range(m)]
# 배열에 담기
for i in range(m):
    a = sys.stdin.readline().split()[0]
    arr.append(list(a))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
white = 0
black = 0

def BFS(i, j, visited):
    queue = deque([[i, j]])
    cnt = 0
    while queue:
        currx, curry = queue.popleft()
        color = arr[currx][curry]
        for d in range(4):
            nx = currx + dx[d]
            ny = curry + dy[d]

            if (nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny] and arr[nx][ny] == color):

                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1 

    if cnt == 0:
        score = 1
    else:
        score = cnt * cnt
    return score, color

for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            score, color = BFS(i, j, visited)
            if color == 'W':
                white += score
            else:
                black += score

print(white, black)