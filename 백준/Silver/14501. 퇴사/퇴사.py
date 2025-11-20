import sys
input = sys.stdin.readline

n = int(input())

arr = [[0, 0]]
for _ in range(n):
    day, cost = map(int, input().split())
    arr.append([day, cost])

dp = [0] * (n + 2)

for i in range(1, n + 1):
    dp[i + 1] = max(dp[i + 1], dp[i])

    day, cost = arr[i]

    if i + day <= n + 1:
        dp[i + day] = max(dp[i + day], dp[i] + cost)

print(max(dp))
