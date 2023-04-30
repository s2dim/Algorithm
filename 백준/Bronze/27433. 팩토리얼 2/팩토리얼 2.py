import sys

n = int(sys.stdin.readline())

a = 1
for i in range(1, n+1):
    a = i * a

print(a)