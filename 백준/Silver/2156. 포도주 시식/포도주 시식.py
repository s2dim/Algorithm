import sys

n = int(input())

arr = [0]
for i in range(n):
    a = int(input())
    arr.append(a)

dp = [0] * (n+1)

dp[1] = arr[1]
if n >= 2:
    dp[2] = arr[1] + arr[2]

if n >= 3:
    for i in range(3, n+1):
        dp[i] = max(max(dp[i-2] + arr[i], dp[i-1]), dp[i-3] + arr[i-1] + arr[i])

print(dp[n])