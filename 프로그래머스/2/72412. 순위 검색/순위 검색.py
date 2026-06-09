from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    dic = defaultdict(list)
    answer = []
    
    for i in info:
        subject, position, year, food, score = i.split(' ')
        
        for s in [subject, '-']:
            for p in [position, '-']:
                for y in [year, '-']:
                    for f in [food, '-']:
                        dic[s+p+y+f].append(int(score))

    for key in dic:
        dic[key].sort()
    
    q = []
    for i in query:
        temp = i.replace('and', '').split()
        score = int(temp.pop())
        key = ''.join(temp)
        answer.append(len(dic[key])-bisect_left(dic[key], score))



    return answer


        

'''

'''