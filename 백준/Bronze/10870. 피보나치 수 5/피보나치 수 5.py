import sys

n = int(sys.stdin.readline())
lst = [0, 1]
for i in range(0, n-1):
    lst.append(lst[i] + lst[i+1])

if n == 0:
    print(0)
else:
    print(lst[-1])
