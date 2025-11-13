import sys

n = int(input())
lst = []

for i in range(n):
    name, k, e, m = sys.stdin.readline().split()
    k = int(k)
    e = int(e)
    m = int(m)

    lst.append([name, k, e, m])

lst = sorted(lst, key = lambda x : (-x[1], x[2], -x[3], ord(x[0][0]), x[0][1:]))

for i in lst:
    print(i[0])