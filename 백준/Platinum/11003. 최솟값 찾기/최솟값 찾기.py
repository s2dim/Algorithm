
import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

dq = deque()

for i in range(n):
    while dq and dq[-1][1] > lst[i]:
        dq.pop()
    dq.append((i, lst[i]))
    if dq[0][0] <= i - l:
        dq.popleft()
    print(dq[0][1], end = ' ')