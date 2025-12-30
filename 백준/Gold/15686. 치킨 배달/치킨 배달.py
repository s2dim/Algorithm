import sys
from itertools import combinations
import copy

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)


chicken = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i+1, j+1))
        if arr[i][j] == 1:
            home.append((i+1, j+1))

dist = [] # 각 집마다 치킨집까지의 거리
for x, y in home:
    lst = []
    for i, j in chicken:
        lst.append(abs(i-x) + abs(j-y))
    dist.append(lst)

lst = [i for i in range(len(chicken))]
comb = list(combinations(lst, m))

min_ = int(1e9)

for i in comb: # (0, 1)
    sum_ = 0
    for j in dist: # []
        temp = int(1e9)
        for k in i:
            temp = min(temp, j[k])
        
        sum_ += temp
    min_ = min(min_, sum_)
            



print(min_)
