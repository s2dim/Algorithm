import sys
from itertools import permutations

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
# 0+ 1- 2* 3/
op = list(map(int, sys.stdin.readline().split()))

def cal(a, b, n):
    if n == 0:
        return a + b 
    elif n == 1:
        return a - b
    elif n == 2:
        return a * b
    elif n == 3:
        if a < 0:
            temp = (a * (-1)) // b
            return temp * (-1)
        else:
            return a // b
    
lst = [i for i, cnt in enumerate(op) for _ in range(cnt)]
lst_cnt = list(set(list(permutations(lst, n-1))))

max_ = -int(1e9)
for i in lst_cnt:
    a = num[0]
    state = True
    for j in range(n-1):
        if (i[j] == 3 and num[j+1] == 0):
            state = False
            break
        else:
            a =  cal(a, num[j+1], i[j])
    max_ = max(a, max_)


min_ = int(1e9)
for i in lst_cnt:
    a = num[0]
    state = True
    for j in range(n-1):
        if (i[j] == 3 and num[j+1] == 0):
            state = False
            break
        else:
            a =  cal(a, num[j+1], i[j])
    if state:
        min_ = min(a, min_)

print(max_)
print(min_)