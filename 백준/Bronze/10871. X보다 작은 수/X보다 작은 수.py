import sys

a, b = map(int, sys.stdin.readline().split())
lst = sys.stdin.readline().split()
lst = list(map(int, lst))

small = []
for i in lst:
    if i < b:
        small.append(i)

print(*small)