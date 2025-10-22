def solution(board):
    dx = [0, 0, -1, -1, -1, 1, 1, 1]
    dy = [-1, 1, -1, 1, 0, -1, 1, 0]
    
    n = len(board)
    visited = [([False] * n) for _ in range(n)]
    print(visited)
    answer = n * n
    
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if (board[i][j] == 1 and not visited[i][j]):
                answer -= 1
                visited[i][j] = True
                
                for d in range(8):
                    nx = i + dx[d]
                    ny = j + dx[d]
                    if (nx >= 0 and nx < n and ny >= 0 and ny < n and 
                        board[nx][ny] == 0 and not visited[nx][ny]):
                        cnt += 1
                        visited[nx][ny] = True
                        
    answer = answer - cnt
    return answer