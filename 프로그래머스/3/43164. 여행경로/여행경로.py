from collections import deque
def solution(tickets):
    # 숫자로 라벨링
    mapping = []
    
    for i in tickets:
        for j in i:
            mapping.append(j)
            
    mapping = list(set(mapping))
    mapping.sort()
    mapping = dict(enumerate(mapping))
    mapping_reverse = {v:k for k,v in mapping.items()}
    
    n = len(mapping)
    graph = [[] for _ in range(n)]
    
    for i in tickets:
        graph[mapping_reverse.get(i[0])].append(mapping_reverse.get(i[1]))
    
    for i in graph:
        i.sort(reverse=True)
        
    visited = [0] * n
    
    for i in range(n):
        visited[i] = len(graph[i])
        

    x = mapping_reverse.get('ICN')
    stack = [x]
    answer = []
    
    while stack:
        cur = stack[-1]
        if graph[cur]:
            nxt = graph[cur].pop()
            stack.append(nxt)
        else:
            answer.append(stack.pop())
    
    answer.reverse()
    
    result = []
    for i in answer:
        result.append(mapping.get(i))
   
    return result