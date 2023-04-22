import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque()

for i in range(1, n+1):
    deq.append(i)

while len(deq) != 1:
        a = deq.popleft()
        b = deq.popleft()
        deq.append(b)

print(deq[0])