import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

set_lst = list(set(lst))
set_lst.sort()
cnt_lst = [i for i in range(len(set_lst))]

dic = dict(zip(set_lst, cnt_lst))

new = []
for i in lst:
    new.append(dic[i])

print(*new)