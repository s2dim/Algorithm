import copy
def solution(m, n, board): # m : 높이, n : 폭
    
    arr = []
    for i in board:
        arr.append([_ for _ in i])
    
    arr = list(map(list, zip(*arr[::-1])))
    
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    
    while True:
        cnt = [0] * n # 빠진 개수 체크 : 형태 (개수)
        big = [0] * n # 최대행
        erase = set()
        
        for x in range(n-1): 
            for y in range(m-1):
                if arr[x][y] == '#':
                    break
                comp = arr[x][y]
                temp = [(x, y)]

                for d in range(3):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if comp == arr[nx][ny]:
                        temp.append((nx, ny))
                    else:
                        break
                if len(temp) == 4:
                    for t in temp:
                        erase.add(t)
        new = []
        if erase:
            for i in erase:
                nowx, nowy = i
                arr[nowx][nowy] = '#'
                cnt[nowy] += 1
                
            for i in arr:
                temp2 = []
                for j in i:
                    if j != '#':
                        temp2.append(j)
                
                temp2 = temp2 + ['#'] * (m - len(temp2))
                new.append(temp2)
            arr = new
                
        else:
            break
            
    answer = 0        
    for i in arr:
        for j in i:
            if j == '#':
                answer += 1

    return answer

'''
BFS로 사방에 있는지 판별
어떻게 내릴 건지 고민

빠진 열 저장 -> lst
내리기 -> 한 번에 내릴 수 있는지 고민... -> 빠진 개수만큼 내림 될 듯
삭제 & 빠진 열 저장 

stack이 빌 때까지 반복

빠진 개수는 어떻게 판별? -> 리스트

- 어디까지 내릴지? lst[0] 기준 정렬, 큰 수 이하라면 내려
(수, 개수 저장)

'''