import heapq

# 지역 수 n, 길 정보 roads, 부대원이 위치한 지역 sources, 강철부대 지역 destination
def solution(n, roads, sources, destination):
    
    inf = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [inf] * (n+1)

    for i in roads:
        a, b = i
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    
    def dijkstra(start):
        queue = []
        distance[start] = 0
        heapq.heappush(queue, (0, start))
        
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
        

        return distance
    
    answer = []
    ans = dijkstra(destination)
    for i in sources:
        answer.append(ans[i] if ans[i] < inf else -1)
        

    return answer

'''
sources의 원소 순대로 최단 시간 부대 복귀
복귀 불가능한 경우도 ㅇ

answer = 복귀까지 최단 시간

'''