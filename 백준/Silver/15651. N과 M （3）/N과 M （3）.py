import sys

m, n = map(int, sys.stdin.readline().split())

lst = []

def cal():
    if len(lst) < n:
        for i in range(1, m+1):
            lst.append(i)
            cal()
            lst.pop()

    else:
        print(*lst)

cal()