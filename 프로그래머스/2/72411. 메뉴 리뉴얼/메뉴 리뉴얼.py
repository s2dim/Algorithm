from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    lst = [[] for i in range(len(course))]
    
    orders = [''.join(sorted(i)) for i in orders]
    
    for i in orders:
        for j in range(len(course)):
            if len(i) >= course[j]:
                for k in combinations(i, course[j]):
                    lst[j].append(''.join(sorted(k)))
    temp = []
    for i in lst:
        temp.append(Counter(i))

    for i in temp:
        if len(i) >= 1:
            max_ = max(i.values())
        for k, v in i.items():
            if v == max_ and v >= 2:
                answer.append(k)
    answer.sort()
    return answer

'''
코스요리 메뉴 : 최소 2가지 이상의 단품 메뉴
최소 2명 이상 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 후보에 포함


'''