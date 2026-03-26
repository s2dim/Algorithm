import sys
from collections import Counter

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

cnt = [0] * (max(lst) + 1)

start = 0
end = 0
answer = 0


while end < n:
    
    if cnt[lst[end]] < k:
        cnt[lst[end]] += 1
        end += 1

    else:
        cnt[lst[start]] -= 1
        start += 1

    answer = max(answer, end - start)
print(answer)