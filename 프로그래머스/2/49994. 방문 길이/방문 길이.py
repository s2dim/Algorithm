def solution(dirs):
    move = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1,0)}
    visited = set()
    x, y = 0, 0
    
    for d in dirs:
        dx, dy = move[d]
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(((nx, ny), (x, y)))
            visited.add(((x, y), (nx, ny)))
            x, y = nx, ny
    return len(visited) // 2