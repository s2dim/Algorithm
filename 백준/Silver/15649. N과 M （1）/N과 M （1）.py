import sys
from itertools import permutations

m, n = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, m + 1)]

answer = list(permutations(lst, n))

for i in answer:
    print(*i)

