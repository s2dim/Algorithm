import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
dp = [1] * n 

for i in range(n):
    for j in range(i):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))
