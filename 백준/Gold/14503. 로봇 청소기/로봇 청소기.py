import sys

dx = [-1, 0, 1, 0] # 위0 왼1 아2 오3 
dy = [0, -1, 0, 1]

n, m = map(int, sys.stdin.readline().split())
r, c, t = map(int, sys.stdin.readline().split())

# 방향 조정
if t == 0:
    t = 0
elif t == 1:
    t = 3
elif t == 2:
    t = 2
elif t == 3:
    t = 1

arr = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)


cnt = 0
state = True

while state:
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1

    for d in range(5):
        if d == 4: # 한 바퀴 다 돈 경우
            t += 2 # 반대 방향
            t = t % 4
            nx = r + dx[t]
            ny = c + dy[t]
            
            # 벽 부딪힘
            if (arr[nx][ny] == 1 or nx < 0 or nx >= n or ny < 0 or ny >= m):
                state = False
                break
            else:
                r = nx
                c = ny
                t += 2
                t = t % 4
                break

        t += 1
        t = t % 4
        nx = r + dx[t]
        ny = c + dy[t]

        if (nx >= 0 and nx < n and ny >= 0 and ny < m):
            if arr[nx][ny] == 0:
                r = nx
                c = ny
                break

print(cnt) 