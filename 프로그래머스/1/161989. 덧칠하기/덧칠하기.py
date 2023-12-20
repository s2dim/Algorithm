def solution(n, m, section):
    
    paint = section[0] - 1
    answer = 0
    
    for i in section:
        if paint < i:
            paint = i + m - 1
            answer += 1
            

    return answer

