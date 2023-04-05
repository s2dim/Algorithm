import sys
from itertools import combinations

a, b = map(int, sys.stdin.readline().split())
lst = sys.stdin.readline().split()
lst = [int(i) for i in lst]

com = []
for i in combinations(lst, 3):
    com.append(i)

com = [sum(com[i]) for i in range(len(com))]
com.sort(reverse=True)


for i in com:
    if b >= i:
        print(i)
        break