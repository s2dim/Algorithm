from collections import deque

def solution(m, n, puddles):
    
    dx = [1, 0]
    dy = [0, 1]
    
    arr = [[0] * (m+1) for _ in range(n+1)]
    visited = [[0] * (m+1) for _ in range(n+1)]
    check = [[False] * (m+1) for _ in range(n+1)]
    
    for x, y in puddles:
        arr[y][x] = 1

    
    queue = deque([(1, 1)])
    visited[1][1] = 1
    check[1][1] = True
    
    while queue:
        currx, curry = queue.popleft()
        
        for d in range(2):
            nx = currx + dx[d]
            ny = curry + dy[d]

            if nx <= n and ny <= m and nx > 0 and ny > 0 and visited[nx][ny] == 0 and not check[nx][ny]:
                print(nx, ny)
                if arr[nx][ny] != 1:
                    visited[nx][ny] = visited[nx-1][ny] + visited[nx][ny-1]
                    
                check[nx][ny] = True
                queue.append((nx, ny))
                
                if (nx, ny) == (n, m):
                    return (visited[n][m]) % 1000000007
    