import sys

lst = []
for i in range(10):
    a = int(sys.stdin.readline())
    b = a % 42
    lst.append(b)

set_lst = set(lst)
print(len(set_lst))