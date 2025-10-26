n = int(input())

stair = [0]
dp = [0] * (n+1)

for i in range(n):
    a = int(input())
    stair.append(a)

dp[0] = stair[0]
dp[1] = stair[1]

if n >= 2:
    dp[2] = dp[1] + stair[2]

if n >= 3:
    for i in range(3, n + 1):
        if (i == n):
            dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[n])