def solution(answers):
    
    first = [1, 2, 3, 4, 5] * 10000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    
    f_n = 0
    s_n = 0
    t_n = 0
    
    
    for i in range(len(answers)):
        if answers[i] == first[i]:
            f_n += 1
        if answers[i] == second[i]:
            s_n += 1
        if answers[i] == third[i]:
            t_n += 1
            
    lst = [f_n, s_n, t_n]
    top = max(lst)
    
    answer = []
    for i in range(3):
        if lst[i] == top:
            answer.append(i+1)
    return answer