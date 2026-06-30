def solution(dirs):
    # 배열 재정의 0~11 * 0~11 (시작점 5, 5)
    arr = [[[] for i in range(11)] for j in range(11)]
    answer = 0
    
    def check(nx, ny):
        if nx >= 0 and nx < 11 and ny >= 0 and ny < 11:
            return True
        else:
            return False
        
    def direction(d, x, y):
        if d == 'L':
            nx = x
            ny = y - 1
        elif d == 'R':
            nx = x
            ny = y + 1
        elif d == 'U':
            nx = x - 1
            ny = y
        elif d == 'D':
            nx = x + 1
            ny = y
            
        if check(nx, ny):
            return [nx, ny]
        else:
            return [x, y]
        
    nowx, nowy = (5, 5)
    for d in dirs:
        old = (nowx, nowy)
        nowx, nowy = direction(d, nowx, nowy)
        
        if old != (nowx, nowy):
            state = False
            for i in arr[nowx][nowy]:
                if i == old:
                    state = True
                    break
            for i in arr[old[0]][old[1]]:
                if i == (nowx, nowy):
                    state = True
                    break
                    
            if not state:
                arr[nowx][nowy].append(old)
                arr[old[0]][old[1]].append((nowx, nowy))
                answer += 1
        


    return answer