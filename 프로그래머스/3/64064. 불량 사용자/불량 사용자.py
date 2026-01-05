from collections import deque, Counter
from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    
    def diff(a, b):
        if len(a) != len(b):
            return False
        else:
            a = [i for i in a]
            b = [i for i in b]
            
            for i in range(len(a)):
                if b[i] == '*' or a[i] == b[i]:
                    continue
                else:
                    return False
            return True
    
    set_ = set()
    for i in list(permutations(user_id, len(banned_id))):
        cnt = 0
        for j in range(len(banned_id)):
            if not diff(i[j], banned_id[j]):
                break
            else:
                cnt += 1
        if cnt == len(banned_id):
            temp = set()
            for k in i:
                temp.add(k)
            set_.add(frozenset(temp))
    
    return len(set_)

'''
- 아이디 당 최소 하나 이상 *
- 제재 아이디 목록 몇 가지 경우의 수?


'''