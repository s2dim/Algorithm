def solution(answers):
    
    first = [1, 2, 3, 4, 5] # 0, 1, 2, 3, 4 -> n % 5
    second = [2, 1, 2, 3, 2, 4, 2, 5] # n % 8
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # n % 10
    
    score1, score2, score3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            score1 += 1
        if answers[i] == second[i % 8]:
            score2 += 1
        if answers[i] == third[i % 10]:
            score3 += 1
    
    max_ = max(max(score1, score2), score3)
    
    answer = []
    
    if max_ == score1:
        answer.append(1)
        
    if max_ == score2:
        answer.append(2)
        
    if max_ == score3:
        answer.append(3)    
    
    return answer