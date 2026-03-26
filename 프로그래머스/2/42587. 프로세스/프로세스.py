import heapq
from collections import deque

def solution(priorities, location):
    answer = -1
    queue = deque([])
    hq = []
    
    for i in range(len(priorities)):
        queue.append(((-1) * priorities[i], i)) # -우선순위, 인덱스
        heapq.heappush(hq, (-1) * priorities[i])

    q = queue.popleft()
    cnt = 1
    

    while True:
        now = heapq.heappop(hq)
        
        while q[0] != now:
        
            queue.append(q)
            q = queue.popleft()

        if q[1] == location:
            answer = cnt
            break
        else:
            q = queue.popleft()
            cnt += 1

        
    return answer

'''
[a, b, c, d]
[2, 1, 3, 2]

숫자가 클수록 우선순위가 높음
'''