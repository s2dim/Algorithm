def solution(n, costs):
    
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    edges = []
    
    for i in costs:
        a, b, cost = i
        edges.append((cost, a, b))
    
    parent = [0] * (n+1)
    
    for i in range(1, n+1):
        parent[i] = i
        
    edges.sort()
    result = 0
    
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            result += cost
    
    return result


'''
n개의 섬 사이에 다리 건설하는 비용 cost
최소 비용으로 모든 섬이 서로 통행 가능하도록 -> 크루스칼

'''