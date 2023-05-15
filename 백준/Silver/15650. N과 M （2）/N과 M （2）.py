import sys
from itertools import combinations

m, n = map(int, sys.stdin.readline().split())


lst = [i for i in range(1, m + 1)]

answer = list(combinations(lst, n))

for i in answer:
    print(*i)

