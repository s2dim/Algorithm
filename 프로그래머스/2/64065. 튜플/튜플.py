from collections import Counter

def solution(s):
    answer = []
    lst = []
    s = s[1:-1]
    n = s.count('}')
    
    for i in range(n):
        idx = 0
        s = s.strip('{')
        while s[idx] != '}':
            idx += 1
        temp = s[:idx]
        temp_lst = temp.split(',')
        temp_lst = [int(i) for i in temp_lst]
        lst.append(temp_lst)
        s = s[idx+2:]

    lst = sorted(lst, key = lambda x:len(x))
    
    for i in lst:
        for j in range(len(i)):
            if i[j] not in answer:
                answer.append(i[j])
    return answer