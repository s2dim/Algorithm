import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    w = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    max_ = sorted(w, reverse=True)
    w[m] = str(w[m])
  
    cnt = 0
    w[m] = str(w[m])
    
    for i in range(len(max_)):

        while int(w[0]) != max_[i]:
            w = w[1:] + [w[0]]
            
        a = w.pop(0)
        cnt += 1
        if isinstance(a, str) == True:
            break
    print(cnt)