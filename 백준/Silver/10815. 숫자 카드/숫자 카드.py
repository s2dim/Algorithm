import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

new = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

lst = []

s1 = set(a)
s2 = set(b)

s = s1 & s2

for i in range(new):
    lst.append(1 if b[i] in s else 0)

print(*lst)