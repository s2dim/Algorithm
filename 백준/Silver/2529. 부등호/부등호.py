import sys
from itertools import permutations

k = int(input())
lst = list(sys.stdin.readline().split())
num = [i for i in range(0, 10)]

min_ = int(1e10)
max_ = -int(1e10)

def sign(a, b, sig):
    if sig == '>':
        if a > b:
            return 1
        else:
            return 0
    elif sig == '<':
        if a < b:
            return 1
        else:
            return 0
        
per = list(permutations(num, k+1))

for i in per:
    now = i[0]
    state = True
    for j in range(k):
        temp = sign(now, i[j+1], lst[j])
        if temp == 0:
            state = False
            break
        else:
            now = i[j+1]
    if state:
        comp = int(''.join([str(n) for n in i]))

        min_ = min(min_, comp)
        max_ = max(max_, comp)

if len(str(min_)) < k+1:
    min_ = '0' + str(min_)

print(max_)
print(min_)
