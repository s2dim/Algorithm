import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())

inf = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b))

queue = deque([x])
distance[x] = 0

while queue:
    q = queue.popleft()

    for i in graph[q]:
        if distance[i] == -1:
            distance[i] = distance[q] + 1
            queue.append(i)

answer = []

for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)



