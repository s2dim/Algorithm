import sys

a = sys.stdin.readline()
num = [a[i] for i in range(len(a))]

lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

idx = []
for i in num:
    for j in range(len(lst)):
        if i in lst[j]:
            idx.append(j)

idx = [idx[i] + 3 for i in range(len(idx))]

print(sum(idx))