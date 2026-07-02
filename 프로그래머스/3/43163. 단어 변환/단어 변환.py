from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque([(begin, 0)])
    n = len(begin)
    
    while queue:
        q, idx = queue.popleft()
        
        if q == target:
            return idx
        if idx >= len(words):
            return 0
        
        for i in words:
            cnt = 0
            for j in range(n):
                if q[j] == i[j]:
                    cnt += 1
            if cnt == n-1:
                queue.append((i, idx+1))
    

    return answer