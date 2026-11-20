def solution(park, routes):
    arr = [list(i) for i in park]

    x = len(park)
    y = len(park[0])
    
    # 시작 위치 탐색
    for i in range(x):
        for j in range(y):
            if arr[i][j] == 'S':
                now = [i, j]
                break
    
    dx = [-1, 1, 0, 0] # W E N S
    dy = [0, 0, -1, 1]
    
    for i in routes:
        direction, move = i.split(' ')
        temp = now # 이동 취소를 위해 저장
        for m in move:
            if direction == 'W':
                nx = dx[0] + now[0]
                ny = dy[0] + now[1]

            elif direction == 'E':
                nx = dx[1] + now[0]
                ny = dy[1] + now[1]

            elif direction == 'N':
                nx = dx[2] + now[0]
                ny = dy[2] + now[1]

            elif direction == 'S':
                nx = dx[3] + now[0]
                ny = dy[3] + now[1]

            if nx < 0 or ny < 0 or nx >= x or ny >= y or arr[nx][ny] == 'X':
                now = temp
                break
            else:
                now = [nx, ny]

    
    return now