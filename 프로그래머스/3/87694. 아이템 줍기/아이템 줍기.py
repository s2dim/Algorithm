from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    arr = [[0] * 102 for _ in range(102)]
    visited =[[0] * 102 for _ in range(102)]
    
    # 좌표 전처리
    rectangle = [[x1 * 2, x2 *2, y1 * 2, y2 *2] for x1, x2, y1, y2 in rectangle]
    characterX = characterX * 2
    characterY = characterY * 2
    itemX = itemX * 2
    itemY = itemY * 2
            
    for i in rectangle:
        x1, y1, x2, y2 = i

        for x in range(x1, x2+1):
            arr[x][y1] = 1 if arr[x][y1] == 0 else arr[x][y1]
            arr[x][y2] = 1 if arr[x][y2] == 0 else arr[x][y2]


        for y in range(y1, y2+1):
            arr[x1][y] = 1 if arr[x1][y] == 0 else arr[x1][y]
            arr[x2][y] = 1 if arr[x2][y] == 0 else arr[x2][y]

    
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                arr[x][y] = 2
                

    queue = deque([[characterX, characterY]])
    
    while queue:
        currx, curry = queue.popleft()

        if currx == itemX and curry == itemY:
            
            return visited[currx][curry] // 2
            
        for d in range(4):
            nx = currx + dx[d]
            ny = curry + dy[d]
            
            if (nx >= 0 and nx <= 102 and ny >= 0 and ny <= 102 and
               arr[nx][ny] == 1 and visited[nx][ny] == 0):
                queue.append([nx, ny])
                visited[nx][ny] = visited[currx][curry] + 1


'''
좌측 하단 (x1, y1) 우측 상단 (x2, y2)
(x1, y1), (x2, y1), (x1, y2), (x2, y2)


'''