from collections import Counter

def solution(clothes):
    
    lst = []
    for i in range(len(clothes)):
        lst.append(clothes[i][1])
        
    counter = Counter(lst)
    new = list(counter.values())
    
    a = 1
    for i in range(len(new)):
        b = new[i] + 1
        a = a * b

    return a - 1