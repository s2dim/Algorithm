from collections import deque

def solution(board):
    dx = [-1, 1, 0, 0] # 좌 우 하 상
    dy = [0, 0, 1, -1]
    
    m = len(board) # 5
    n = len(board[0]) # 7
    
    
    arr = []
    visited = [[False] * n for _ in range(m)]
    
    for i in range(len(board)):
        temp = []
        for j in range(len(board[0])):
            if board[i][j] == 'D':
                temp.append(-1)
            elif board[i][j] == 'R':
                x, y = (i, j)
                temp.append(0)
            elif board[i][j] == 'G':
                a, b = (i, j)
                temp.append(0)
            else:
                temp.append(0)
                
        arr.append(temp)
    
    
    queue = deque([])
    
    # 초기값 셋팅
    queue.append((x, y, 0))    
    visited[x][y] = True
    
    while queue:
        arrx, arry, cnt = queue.popleft()
        
        if (arrx, arry) == (a, b):
            return cnt
        
        for d in range(4):
            nx = arrx + dx[d]
            ny = arry + dy[d]
            
            if nx < m and ny < n and nx >= 0 and ny >= 0 and arr[nx][ny] == 0:
                
                while nx + dx[d] < m and ny + dy[d] < n and nx + dx[d] >= 0 and ny + dy[d] >= 0 and arr[nx+dx[d]][ny+dy[d]] == 0:
                    nx = nx + dx[d]
                    ny = ny + dy[d]
                    # 갈 수 있는 만큼 가기 (2칸 이상)
                
                if not visited[nx][ny]:
                    visited[nx][ny] = True    
                    queue.append((nx, ny, cnt+1)) # 한 칸이라도 움직였다
    


    return -1