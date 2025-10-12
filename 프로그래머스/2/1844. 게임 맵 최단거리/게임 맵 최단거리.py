from collections import deque

def solution(maps):
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    n = len(maps)
    m = len(maps[0])
    
    arr = [[0] * (m+1) for _ in range(n+1)]
    visited = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            arr[i+1][j+1] = maps[i][j]
    

    queue = deque([[1, 1]])
    visited[1][1] = 1
    
    while queue:
        currx, curry = queue.popleft()
        
        if currx == n and curry == m:
            return visited[currx][curry]
        
        for d in range(4):
            nx = currx + dx[d]
            ny = curry + dy[d]
            
            if (nx > 0 and nx <= n and ny > 0 and ny <= m and
                arr[nx][ny] == 1 and visited[nx][ny] == 0):
                queue.append([nx, ny])
                visited[nx][ny] = visited[currx][curry] + 1
        

    return -1