# 2026-04-06

t = int(input())
lst = []


for i in range(t):
    n = int(input())
    lst.append(n)

max_ = max(lst)

dp = [0] * (max_ + 1)
dp[0] = 1

for i in [1, 2, 3]:
    for j in range(i, max_ + 1):
        dp[j] += dp[j-i]

for i in lst:
    print(dp[i])