import sys

n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
res = 0
min_ = int(1e9)
state = False

while True:
    if res >= s:
        min_ = min(min_, end - start)
        state = True
        res -= lst[start]
        start += 1
    elif end == n:
        break
    else:
        res += lst[end]
        end += 1

print(min_ if state else 0)