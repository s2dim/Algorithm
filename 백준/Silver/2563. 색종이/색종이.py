import sys

n = int(sys.stdin.readline())
lst = []

for i in range(100):
    a = [0 for i in range(100)]
    lst.append(a)

for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    w = w - 1
    h = h - 1

    for j in range(w, w + 10):
        for k in range(h, h + 10):
            lst[j][k] = 1

cnt = sum(lst, [])

print(cnt.count(1))