import sys

basket, num = map(int, sys.stdin.readline().split())

lst = [i+1 for i in range(basket)]
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    a = a - 1
    b = b - 1
    c = lst[a]
    lst[a] = lst[b]
    lst[b] = c

print(*lst)