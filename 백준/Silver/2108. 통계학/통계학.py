import sys
from collections import Counter

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)
lst.sort()
avg = round(sum(lst) / n)
mid_idx = n // 2
mid = lst[mid_idx]
counter = Counter(lst)
max_val = max(counter.values())
max_key = [k for k, v in counter.items() if v == max_val]
if len(max_key) > 1:
    max_key.sort()
    max_ = max_key[1]
else:
    max_ = max_key[0]
rge = max(lst) - min(lst)

print(avg)
print(mid)
print(max_)
print(rge)