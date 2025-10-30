def solution(rows, columns, queries):
    
    # 좌표 맞추기 위해 배열에 다시 담기
    arr = [[0] * (columns + 1) for _ in range(rows + 1)]
    
    # 배열 입력
    start = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            arr[i][j] = start
            start += 1
    
    answer = []
    # x1, y1부터 시작
    for i in queries:
        x1, y1, x2, y2 = i
        
        start = arr[x1][y1]
        min_ = start

        # 위로
        for x in range(x1, x2):
            arr[x][y1] = arr[x+1][y1]
            min_ = min(min_, arr[x][y1])
        # 왼쪽
        for y in range(y1, y2):
            arr[x2][y] = arr[x2][y+1]
            min_ = min(min_, arr[x2][y])
            
        # 아래쪽
        for x in range(x2, x1, -1):
            arr[x][y2] = arr[x-1][y2]
            min_ = min(min_, arr[x][y2])
            
        # 오른쪽
        for y in range(y2, y1, -1):
            arr[x1][y] = arr[x1][y-1]
            min_ = min(min_, arr[x1][y])
            
        arr[x1][y1+1] = start
    
        answer.append(min_)

    return answer
'''

대상 열 : (x1, y1) ~ (x2, y1) 위로 / 오른쪽
대상 열 : (x2, y1) ~ (x2, y2) 왼쪽 / 위로
대상 열 : (x1, y2) ~ (x2, y2) 내려 / 왼쪽
대상 열 : (x1, y1) ~ (x1, y2) 오른쪽 / 내려



대상 열 : (x1, y1) ~ (x1, y2) 오른쪽 / 내려
대상 열 : (x1, y2) ~ (x2, y2) 내려 / 왼쪽
대상 열 : (x2, y1) ~ (x2, y2) 왼쪽 / 위로
대상 열 : (x1, y1) ~ (x2, y1) 위로 / 오른쪽

(2, 2) (2, 3) (2, 4)
(3, 2) 
(4, 2)
(5, 2) (5, 3) (5, 4)
'''

'''
(2, 2) (5, 4)
(x1, y1) (x2, y2)

세로 : (x2 - x1 + 1) 
가로 : (y2 - y1 + 1)

리스트에 범위 숫자 담기
움직이기


끄트머리 : 

(2, 2) (2, 3) (2, 4)
(3, 2) 
(4, 2)
(5, 2) (5, 3) (5, 4)

'''