def solution(n, wires):
    arr = [[0] * (n+1) for _ in range(n+1)]
    
    for w in wires:
        a, b = w
        arr[a][b] = 1
        arr[b][a] = 1
    
    min_ = n
    
    # 전선 끊기
    for w in wires:
        a, b = w
        arr[a][b] = 0
        arr[b][a] = 0
        
        cnt = 0
        visited = [False] * (n+1)
        stack = [1]
        
        while stack:
            s = stack.pop()
            for i in range(1, n+1):
                if arr[s][i] == 1 and not visited[i]:
                    cnt += 1
                    visited[i] = True
                    stack.append(i)
        
        cnt2 = n - cnt
        arr[a][b] = 1
        arr[b][a] = 1
        min_ = min(min_, abs(cnt2 - cnt))        
    
    return min_



'''

'''