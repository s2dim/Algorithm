import sys

lst = []
max_lst = []

for i in range(9):

    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)
    max_lst.append(max(a))

max_num = max(max_lst)
row = max_lst.index(max_num)
column = lst[row].index(max_num)
print(max_num)
print(row + 1, column + 1)