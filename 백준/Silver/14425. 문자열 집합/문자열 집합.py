import sys

n, m = map(int, sys.stdin.readline().split())

lst1 = []
lst2 = []

for i in range(n):
    a = sys.stdin.readline()
    lst1.append(a)

s1 = set(lst1)

for i in range(m):
    b = sys.stdin.readline()
    lst2.append(b)

s2 = set(lst2)

s = s1 & s2

cnt = 0
for i in range(len(lst2)):
    if lst2[i] in s:
        cnt += 1

print(cnt)