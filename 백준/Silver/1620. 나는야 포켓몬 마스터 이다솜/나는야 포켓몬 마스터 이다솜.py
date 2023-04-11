import sys

m, n = map(int, sys.stdin.readline().split())

name = {}
num = {}

for i in range(1, m + 1):
    a = sys.stdin.readline().strip()
    name[a] = i
    num[i] = a

for i in range(n):
    a = sys.stdin.readline().strip()
    if a.isdigit() == True:
        print(num[int(a)])
    else:
        print(name[a])

