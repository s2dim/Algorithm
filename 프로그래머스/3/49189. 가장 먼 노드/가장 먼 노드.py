import heapq
from collections import Counter
def solution(n, vertex):
    
    inf = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [inf] * (n+1)
    
    for i in vertex:
        a, b = i
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            to_v = i[0]
            cost = dist + i[1]
            
            if cost < distance[to_v]:
                distance[to_v] = cost
                heapq.heappush(queue, (cost, to_v))

    lst = Counter(distance[1:])

    return lst[max(lst)]


'''

'''