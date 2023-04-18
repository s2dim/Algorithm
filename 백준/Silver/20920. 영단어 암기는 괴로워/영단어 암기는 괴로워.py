import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

lst = []
for i in range(n):
    a = sys.stdin.readline().strip()
    if len(a) >= m:
        lst.append(a)

counter = Counter(lst)

result = sorted(counter.items(), key=lambda x:(x[0]))
result.sort(key=lambda x:(x[1], len(x[0])), reverse=True)


for i in range(len(result)):
    print(result[i][0])