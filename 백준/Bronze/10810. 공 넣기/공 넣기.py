import sys

basket, num = map(int, sys.stdin.readline().split())
arr = [0 for i in range(basket)]

for i in range(num):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(a-1, b):
        arr[j] = c

print(*arr)