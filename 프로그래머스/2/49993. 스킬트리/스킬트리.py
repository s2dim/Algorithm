def solution(skill, skill_trees):
    lst = [-1] * len(skill_trees)
    
    s = list(skill)
    idx = 0
    for i in skill_trees:
        for j in i:
            if j in s:
                temp = s.index(j)
                if lst[idx] + 1 == temp:
                    lst[idx] = temp
                else:
                    lst[idx] = -2
                    break
                
        idx += 1
    
    cnt = 0
    for i in lst:
        if i != -2:
            cnt += 1
                
    return cnt