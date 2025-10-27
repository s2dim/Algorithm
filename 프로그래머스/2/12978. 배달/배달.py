import heapq

# 마을 개수 N,  (a, b, 소요시간)
def solution(N, road, K):
    inf = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [inf] * (N+1)
    
    for i in road:
        a, b, c = i
        graph[a].append((b, c))
        graph[b].append((a, c))
    
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
        
    
    answer = 0
    
    for i in range(1, N+1):
        if distance[i] != inf and distance[i] <= K:
            answer += 1

    print(distance)
    return answer