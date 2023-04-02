import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
total = []
for i in range(2 * n):
    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)

for i in range(n):
    print(*[a + b for a, b in zip(lst[i],lst[i+n])])