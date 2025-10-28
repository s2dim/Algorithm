import sys
import heapq
n, m, k, x = map(int, sys.stdin.readline().split())

inf = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

# 다익스트라
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

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

arr = dijkstra(x)
answer = []

for i in range(len(arr)):
    if arr[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
