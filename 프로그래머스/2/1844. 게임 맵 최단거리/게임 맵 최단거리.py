from collections import deque

def solution(maps):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]
    
    n = len(maps)
    m = len(maps[0])
  
    arr = [[0] * (m+1) for _ in range(n+1)] # 좌표 맞춘 배열
    visited = [[0] * (m+1) for _ in range(n+1)]
    
    # 좌표에 맞춰 다시 담기
    for i in range(n):
        for j in range(m):
            arr[i+1][j+1] = maps[i][j]

    
    queue = deque([(1, 1)])
    visited[1][1] = 1
    
    while queue:
        curr_x, curr_y = queue.popleft()
        
        if curr_x == n and curr_y == m:
            return visited[curr_x][curr_y]
        
        for d in range(4):
            nx = curr_x + dx[d]
            ny = curr_y + dy[d]

            if (nx > 0 and nx <= n and ny > 0 and ny <= m 
                and arr[nx][ny] == 1 and visited[nx][ny] == 0):
                queue.append([nx, ny])
                visited[nx][ny] = visited[curr_x][curr_y] + 1

    
    return -1