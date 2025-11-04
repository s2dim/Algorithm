import sys
from collections import deque

# 시계
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
k = int(input())

arr = [[0] * n for _ in range(n)]
state = True

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    arr[x-1][y-1] = 1 # 사과 배정
arr[0][0] = 2

nx, ny, t = 0, 0, 0 # 초기값 셋팅
d = 3


path = deque([[0, 0]])

l = int(input())
for _ in range(l):
    a, b = sys.stdin.readline().split()
    a = int(a)

    while t < a:
        if not state:
            break

        nx = nx + dx[d]
        ny = ny + dy[d]

        if (nx >= 0 and nx < n and ny >= 0 and ny < n):
            if arr[nx][ny] == 1: # 사과인 경우 +1
                t += 1
                arr[nx][ny] = 2
                path.appendleft([nx, ny])
            elif arr[nx][ny] == 0:
                t += 1
                arr[nx][ny] = 2
                tx, ty = path.pop()
                arr[tx][ty] = 0
                path.appendleft([nx, ny])
            elif arr[nx][ny] == 2:
                state = False
                break
    
        else:
            state = False
            break

    if b == 'L':
        d = (d-1) % 4
    elif b == 'D':
        d = (d+1) % 4
        

while state:
    nx = nx + dx[d]
    ny = ny + dy[d]

    if (nx >= 0 and nx < n and ny >= 0 and ny < n):
        if arr[nx][ny] == 1: # 사과인 경우 +1
            t += 1
            arr[nx][ny] = 2
            path.appendleft([nx, ny])
        elif arr[nx][ny] == 0:
            t += 1
            arr[nx][ny] = 2
            tx, ty = path.pop()
            arr[tx][ty] = 0
            path.appendleft([nx, ny])
        elif arr[nx][ny] == 2:
            state = False
            break
    else:
        state = False
        break


print(t+1)