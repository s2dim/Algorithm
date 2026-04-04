# 2026-04-04
import sys

n, x = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start = 0
cnt = sum(lst[:x])
end = x - 1
res = []

while end < n - 1:
    res.append(cnt)
    cnt -= lst[start]
    start += 1
    end += 1
    cnt += lst[end]

res.append(cnt)

if max(res) == 0:
    print('SAD')
else:
    print(max(res))
    print(res.count(max(res)))