def solution(left, right):
    
    lst = [i for i in range(left, right+1)]
    
    cnt = 0
    for i in lst:
        new = [j for j in range(1, i+1) if i % j == 0]
        len_new = len(new)
        if len_new % 2 == 0:
            cnt += i
        else:
            cnt -= i
            
    return cnt