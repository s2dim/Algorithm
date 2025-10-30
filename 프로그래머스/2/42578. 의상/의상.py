from collections import defaultdict
from math import prod

def solution(clothes):

    dic = defaultdict(list)
    for i in clothes:
        item = i[0]
        category = i[1]

        dic[category].append(item)
    
    lst = list(dic.values())
    answer = prod((len(i) + 1) for i in lst)
    return answer - 1
    
'''
의상 중 일부가 다르면 다른 옷


'''