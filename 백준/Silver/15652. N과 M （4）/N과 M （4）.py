import sys

m, n = map(int, sys.stdin.readline().split())

lst = []

def cal(a):
    if len(lst) < n:
        for i in range(a, m+1):
            lst.append(i)
            cal(i)
            lst.pop()

    else:
        print(*lst)

cal(1)