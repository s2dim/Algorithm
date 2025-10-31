def solution(triangle):
    n = len(triangle)
    
    dp = [[0] * (n) for _ in range(n)]
    
    dp[0][0] = triangle[0][0]
    
    if n >= 2:
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    op1 = dp[i-1][j-1] + triangle[i][j]
                    op2 = dp[i-1][j] + triangle[i][j]
                    dp[i][j] = max(op1, op2)
    
    answer = max(dp[n-1])
    return answer

'''
끄트머리 -> 걍 내려옴
'''