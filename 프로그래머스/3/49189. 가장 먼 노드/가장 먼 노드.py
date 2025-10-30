import heapq
from collections import Counter

def solution(n, vertex):
    
    inf = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [inf] * (n+1)
    
    for a, b in vertex:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    heap = []
    heapq.heappush(heap, (0, 1))
    distance[1] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            to_v = i[0]
            cost = dist + i[1]
            
            if cost < distance[to_v]:
                distance[to_v] = cost
                heapq.heappush(heap, (cost, to_v))
                
    max_ = max(distance[1:])
    cnt = Counter(distance[1:])
    
    return cnt.get(max_)