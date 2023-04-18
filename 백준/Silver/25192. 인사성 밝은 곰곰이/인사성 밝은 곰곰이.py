import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    lst.append(sys.stdin.readline().strip())

idx = []
for i in range(len(lst)):
    if lst[i] == 'ENTER':
        idx.append(i)
cnt = 0
idx = idx + [len(lst)]
for i in range(len(idx)-1):
    start = idx[i] + 1
    end = idx[i+1]
    
    new = lst[start:end]
    cnt_lst = set(new)
    cnt += len(cnt_lst)

print(cnt)