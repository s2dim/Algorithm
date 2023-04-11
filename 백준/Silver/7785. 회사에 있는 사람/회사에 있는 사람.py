import sys

n = int(sys.stdin.readline())

dic = {}
for i in range(n):
    name, state = sys.stdin.readline().split()
    dic[name] = state

lst = [k for k, v in dic.items() if v == 'enter']
lst.sort(reverse=True)

for i in lst:
    print(i)