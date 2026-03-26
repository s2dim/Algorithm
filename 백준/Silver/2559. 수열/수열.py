import sys

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

max_ = -int(1e9)

start = 0
end = k-1
res = sum(lst[:k])
max_ = max(max_, res)

while end < n-1:
    res -= lst[start]
    start += 1
    end += 1
    res += lst[end]
    max_ = max(max_, res)
print(max_)