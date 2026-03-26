import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
res = 0
cnt = 0

while True:
    if res >= m:
        if res == m:
            cnt += 1
        res -= lst[left]
        left += 1
    elif right == n:
        break
    else:
        res += lst[right]
        right += 1
    

print(cnt)