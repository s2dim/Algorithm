def solution(number, k):
    answer = []
    
    for now in number:
        while answer and k > 0:
            if now > answer[-1]:
                answer.pop()
                k -= 1
            else:
                break
                
        answer.append(now)
        
    if k > 0:
        answer = answer[:-k]
            
    return ''.join(answer)