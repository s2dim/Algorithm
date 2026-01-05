from collections import deque

def solution(begin, target, words):
    
    def diff(a, b):
        a = [i for i in a]
        b = [i for i in b]
        
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
            
            if cnt > 1:
                break
        
        if cnt == 1:
            return True
        else:
            return False
    
    if target not in words:
        return 0 
    
    queue = deque([(0, begin)])
    
    while queue:
        dist, q = queue.popleft()
        
        if q == target:
            return dist
        
        if dist > len(words):
            return 0
        
        for i in words:
            if diff(q, i):
                queue.append((dist+1, i))



'''

'''