import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
c = b - 1
lst = [i for i in range(1, a+1)]
new = []

while len(lst) != 0:
    try:
        if c < len(lst):
            new.append(lst.pop(c))
            c += b - 1
        else:
            c = c - len(lst)
            new.append(lst.pop(c))
            c += b - 1
    except:
        continue

print("<" + ', '.join(str(i) for i in new) + ">")