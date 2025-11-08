import sys

n = int(input())
dp = [[0] * (n+1) for _ in range(3)]

lst = list(map(int, sys.stdin.readline().split()))
dp[0][1] = lst[0]
dp[1][1] = lst[1]
dp[2][1] = lst[2]

if n > 1:
    for i in range(2, n+1):
        lst = list(map(int, sys.stdin.readline().split()))

        for j in range(3):
            if j == 0:
                dp[j][i] = min(dp[1][i-1] + lst[0], dp[2][i-1] + lst[0])
            if j == 1:
                dp[j][i] = min(dp[0][i-1] + lst[1], dp[2][i-1] + lst[1])
            if j == 2:
                dp[j][i] = min(dp[0][i-1] + lst[2], dp[1][i-1] + lst[2])

print(min(dp[0][n], dp[1][n], dp[2][n]))