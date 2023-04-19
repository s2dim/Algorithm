def solution(priorities, location):
    max_ = sorted(priorities, reverse=True)
    # dic = {i : priorities[i] for i in range(len(priorities))}
    
    cnt = 0
    lst = []
    priorities[location] = str(priorities[location])
    
    for i in range(len(max_)):

        while int(priorities[0]) != max_[i]:
            priorities = priorities[1:] + [priorities[0]]
            
            # print(priorities)
        a = priorities.pop(0)
        lst.append(a)
        cnt += 1
        if isinstance(a, str) == True:
            break

    return cnt

