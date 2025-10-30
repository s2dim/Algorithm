from collections import deque

def solution(begin, target, words):
    
    # 다른 개수
    def diff(x1, x2):
        cnt = 0
        for i in range(len(x1)):
            if x1[i] != x2[i]:
                cnt += 1             
        return cnt
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    queue = deque([(0, begin)])
    
    while queue:
        dist, now = queue.popleft()

        if diff(now, target) == 1:
            dist += 1
            return dist
        
        for i in range(len(words)):
            if diff(now, words[i]) == 1 and not visited[i]: 
                cost = dist + 1
                queue.append((cost, words[i]))
                visited[i] = True
            

    return 0