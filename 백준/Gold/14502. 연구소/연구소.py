import sys
from collections import Counter
from itertools import combinations
import copy

n, m = map(int, sys.stdin.readline().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

arr = []
max_ = 0

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

# 모든 경우의 수 구하기
safe_zone = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            safe_zone.append((i, j))

combs = list(combinations(safe_zone, 3))

for comb in combs:
    temp_arr = copy.deepcopy(arr)
    visited = [[False] * (m) for _ in range(n)]
    for sx, sy in comb:
        temp_arr[sx][sy] = 1


    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue

            if temp_arr[i][j] == 1:
                visited[i][j] = True
                continue
            
            stack = []
            if temp_arr[i][j] == 2 and not visited[i][j]:
                stack.append((i, j))
                visited[i][j] = True
            
            while stack:
                currx, curry = stack.pop()
                for d in range(4):
                    nx = currx + dx[d]
                    ny = curry + dy[d]
                    if (nx >= 0 and nx < n and ny >= 0 and ny < m and temp_arr[nx][ny] == 0 and not visited[nx][ny]):
                        temp_arr[nx][ny] = 2
                        stack.append((nx, ny))
                        visited[nx][ny] = True

    
    ans = 0
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 0:
                ans += 1

    max_ = max(max_, ans)

print(max_)
