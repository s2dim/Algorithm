import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)

lst.sort()
for i in lst:
    print(*i)