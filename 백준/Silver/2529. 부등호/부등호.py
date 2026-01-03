import sys
from itertools import permutations

k = int(input())
lst = list(sys.stdin.readline().split())
num = [1] * (10)

min_ = None
max_ = None

def sign(a, b, sig):
    if sig == '>':
        return a > b
    else:  # '<'
        return a < b

def dfs(i, now):
    global min_, max_

    # 숫자는 k+1자리
    if i == k + 1:
        if min_ is None or now < min_:
            min_ = now
        if max_ is None or now > max_:
            max_ = now
        return

    for n in range(10):
        if num[n] == 1:
            # 첫 자리면 조건 없이 선택 가능
            # 그 외에는 직전 자리(now[-1])와 n이 lst[i-1]를 만족해야 함
            if i == 0 or sign(int(now[-1]), n, lst[i - 1]):
                num[n] = 0
                dfs(i + 1, now + str(n))
                num[n] = 1

dfs(0, "")

print(max_)
print(min_)