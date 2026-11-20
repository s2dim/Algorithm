def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        stack = []
        if not visited[i]:
            stack.append(i)
            answer += 1
        
        while stack:
            s = stack.pop()
        
            for j in range(len(computers[s])):
                if computers[s][j] == 1 and not visited[j]:
                    stack.append(j)
                    visited[j] = True
            
    return answer
