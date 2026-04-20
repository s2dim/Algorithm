import sys

r, c = map(int, sys.stdin.readline().split())
arr = []

for i in range(r):
    temp = list(sys.stdin.readline().strip())
    arr.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


stack = []
stack.append((0, 0, arr[0][0], 1))

max_ = 1

while stack:
    currx, curry, word, cnt = stack.pop()
    max_ = max(max_, cnt)

    for d in range(4):
        nx = currx + dx[d]
        ny = curry + dy[d]

        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if arr[nx][ny] not in word:
                stack.append((nx, ny, word + arr[nx][ny], cnt + 1))


print(max_)
