import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)

lst.sort()

for i in lst:
    print(i)