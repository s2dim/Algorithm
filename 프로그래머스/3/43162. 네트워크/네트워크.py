def solution(n, computers):
    
    visited = [False] * n
    cnt = 0
    
    for i in range(n):
        stack = []
        if not visited[i]:
            stack.append(i)
            cnt += 1

        while stack:
            s = stack.pop()
            for i in range(n):
                if (computers[s][i] == 1 and not visited[i]):
                    stack.append(i)
                    visited[i] = True
    
        
    return cnt