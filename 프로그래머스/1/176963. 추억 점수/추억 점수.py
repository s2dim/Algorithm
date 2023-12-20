def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        score = 0
        for j in range(len(name)):
            if name[j] in photo[i]:
                score += yearning[j]
        answer.append(score)
        
    return answer