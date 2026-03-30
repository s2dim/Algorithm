from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

queue = deque([])
visited = [False] * 100001

queue.append((n, 0))
visited[n] = True

while queue:
    now, time = queue.popleft()

    if now == k:
        break

    for next in (now - 1, now + 1, now * 2):
        if next <= 100000 and next >= 0 and not visited[next]:
            queue.append((next, time + 1))
            visited[next] = True

print(time)