import sys

n = int(input())
inf = int(1e9)

graph = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    graph.append(a)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = inf

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n):
    for b in range(n):
        if graph[a][b] == inf:
            graph[a][b] = 0
        elif graph[a][b] > 0:
            graph[a][b] = 1
        
        print(graph[a][b], end = ' ')
    print()