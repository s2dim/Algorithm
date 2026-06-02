def solution(s):
    left = 0
    state = False # ( 가 있는지 체크
    
    for i in s:
        if i == ')':
            if not state or left <= 0:
                return False
            else:
                left -= 1
                
        elif i == '(':
            left += 1
            state = True
    
    if left > 0:
        state = False

    return state