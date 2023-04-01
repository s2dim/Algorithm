import sys

num = int(sys.stdin.readline())

for i in range(num):
    lst = list(map(int, sys.stdin.readline().split()))
    a = sum(lst[1:])
    n = lst[0]
    avg = a / n
    cnt = [i for i in lst[1:] if i > avg]
    print("{:.3f}%".format(len(cnt) * 100 / n))