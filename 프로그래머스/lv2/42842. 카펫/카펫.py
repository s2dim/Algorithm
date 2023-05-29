def solution(brown, yellow):
    
    total = brown + yellow

    lst = []
    
    for i in range(3, total+1):
        
        if total % i == 0:
            w = total // i
            h = i

            if (w - 2) * (h - 2) == yellow:
                answer = [h, w]
        
            
    return answer

'''
0 0 0 0
0 @ @ 0
0 @ @ 0
0 0 0 0

b = 12
y = 4
(4, 4)

000000000000
0@@@@@@@@@@0
0@@@@@@@@@@0
000000000000
'''