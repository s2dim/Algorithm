import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    change = [b, a]
    lst.append(change)

lst.sort()
for i in range(len(lst)):
    print(lst[i][1], lst[i][0])
