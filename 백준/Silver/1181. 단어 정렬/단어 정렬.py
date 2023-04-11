import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    a = sys.stdin.readline().strip()
    lst.append(a)

lst = list(set(lst))
lst.sort()
lst.sort(key = lambda x : len(x))

for i in lst:
    print(i)