import sys
import heapq

n, d = map(int, sys.stdin.readline().split())

lst = []
graph = [[] for i in range(d+1)]
inf = int(1e9)
distance = [inf] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1))

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if a <= d and b <= d:
        graph[a].append((b, c))

heap = []
heapq.heappush(heap, (0, 0))
distance[0] = 0

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

print(distance[d])


'''
지름길
시작 위치, 도착 위치, 지름길 길이

'''