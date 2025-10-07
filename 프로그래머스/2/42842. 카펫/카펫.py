def solution(brown, yellow):
    
    all = brown + yellow
    
    for x in range(1, all+ 1):
        if all % x == 0:
            y = all // x

            if (x - 2) * (y - 2) == yellow:
                return [y, x]

            
            
'''
x * y = brown + yellow
(x - 2) * (y - 2) = yellow
x
'''