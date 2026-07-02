def solution(places):
    answer = []
    dx = [0, 1, -1, 0] # 오른쪽 아래 위 왼쪽
    dy = [1, 0, 0, -1]
    
    def cal(p):
        for i in range(5): # 멘헤튼 거리 2 = 대각선, 직선 2칸까지
            for j in range(5):
                if p[i][j] == 'P':
                    
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        
                        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
                            if p[nx][ny] == 'P': 
                                return 0
                            elif p[nx][ny] == 'O': # 오른쪽 아래 위 왼쪽
                                if d == 0:
                                    temp = [0, 1, 2]
                                elif d == 1:
                                    temp = [0, 1, 3]
                                elif d == 2:
                                    temp = [0, 2, 3]
                                elif d == 3:
                                    temp = [1, 2, 3]
                                for d in temp:
                                    nxx = nx + dx[d]
                                    nyy = ny + dy[d]
                                    if nxx >= 0 and nxx < 5 and nyy >= 0 and nyy < 5 and p[nxx][nyy] == 'P': 
                                        return 0
        return 1
    
    for p in places:
        answer.append(cal(p))
                    
    return answer

'''
p끼리의 거리 구하기
그 사이에 뭐가 있는지 보기 (대각선은?) -> 대각선도
'''