import sys

k = int(sys.stdin.readline())

lst = []

for i in range(k):
    a = int(sys.stdin.readline())
    if a == 0:
        lst.pop(-1)


    else:
        lst.append(a)


print(sum(lst))
