import sys

n, k = map(int, sys.stdin.readline().split())


ans = []
lst = [i for i in range(1, n+1)]
now = n
start = 0

for i in range(n):
    start = ((start + k - 1) % now) 
    a = lst.pop(start)
    ans.append(a)
    now -= 1

ans = [str(i) for i in ans]
print("<" +', '.join(ans) + ">")