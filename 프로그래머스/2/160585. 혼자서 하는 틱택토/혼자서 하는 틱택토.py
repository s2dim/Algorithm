def solution(board):
    lboard = list(zip(*board))

    rotate = []
    for i in lboard:
        rotate.append(''.join(i))
    
    def case(board, rotate):
        
        
        # 연속 개수
        stateO = 0
        stateX = 0
        
        for i in board:
            if i == 'OOO':
                stateO += 1
            elif i == 'XXX':
                stateX += 1
                
        for i in rotate:
            if i == 'OOO':
                stateO += 1
            elif i == 'XXX':
                stateX += 1
        
        # 대각선 체크
        crossl = ''
        crossr = ''
        for i in range(3):
            crossl += board[i][i]
            crossr += board[i][2-i]
        

        if crossl == 'OOO':
            stateO += 1
        if crossr == 'OOO':
            stateO += 1
        if crossl == 'XXX':
            stateX += 1
        if crossr == 'XXX':
            stateX += 1
        
        if (stateO == 1 and stateX == 1): # 둘다 3개씩 만든 경우는 없음
            return False
        
        # 개수 체크
        o = 0
        x = 0
        for i in board:
            o += i.count('O')
            x += i.count('X')
    
        if o > x:
            if o-1 != x:
                return False
        if x > o:
            return False
        
        if stateO > 0:
            if o-1 != x:
                return False
        if stateX > 0:
            if o != x:
                return False
    
        return True
    
                
    check1 = case(board, rotate)
    
    if check1:
        return 1
    

    return 0


'''
선공 O 후공 X
1) OOO XXX 있는지 체크 (가로 세로 대각선) 
 1-1) OOO가 있다면 XXX가 있으면 안 됨
 1-2) XXX가 있다면 OOO가 있으면 안 됨
2) O X 개수
 2-1) 같거나 O가 더 많아야 함
 

'''