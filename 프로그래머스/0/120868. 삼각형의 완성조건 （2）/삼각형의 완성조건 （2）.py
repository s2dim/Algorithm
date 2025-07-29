def solution(sides):
    sum_ = sum(sides)
    max_ = max(sides)
    min_ = min(sides)
    
    cnt = 0
    cnt += (sum_ - max_ - 1)
    
    
    for i in range(1, max_ + 1) :
        if min_ + i > max_:
            cnt += 1
    
    return cnt


'''
새로운 변이 가장 긴 경우
새로운 변이 나머지인 경우


'''