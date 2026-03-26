from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    x = len(maps)
    y = len(maps[0])
    
    visited = [[0] * (y) for _ in range(x)]
    
    q = deque([(0, 0)])
    visited[0][0] = 1
    
    while q:
        currx, curry = q.popleft()
        
        for d in range(4):
            nx = dx[d] + currx
            ny = dy[d] + curry  
            
            if nx >= 0 and ny >= 0 and nx < x and ny < y and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[currx][curry] + 1
    
    
    return -1 if visited[x-1][y-1] == 0 else visited[x-1][y-1]

'''
0: 벽 1: 길
'''