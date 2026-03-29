import sys
sys.setrecursionlimit(10**6)

n, d = map(int, sys.stdin.readline().split())

lst = []
graph = [[] for i in range(d+1)]

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if a <= d and b <= d:
        graph[a].append((b, c))


def shortcut(idx, cost):
    if idx == d:
        return cost
    if idx > d:
        return int(1e9)
    result = shortcut(idx+1, cost+1)
    
    if graph[idx]:
        for i in graph[idx]:
            result = min(result, shortcut(i[0], cost+i[1]))
    return result

print(shortcut(0, 0))

'''
지름길
시작 위치, 도착 위치, 지름길 길이

'''