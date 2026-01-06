from collections import deque

def solution(x, y, n):
    inf = int(1e9)
    lst = [inf] * (y+1)
    
    lst[x] = 0
    queue = deque([])
    queue.append(x)
    
    while queue:
        q = queue.popleft()
        for cal in (q + n, q * 2, q * 3):
            if cal <= y and lst[cal] > lst[q] + 1:
                lst[cal] = lst[q] + 1
                queue.append(cal)
    
    return -1 if lst[y] == inf else lst[y]