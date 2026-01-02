def solution(numbers, target):
    result = 0
    def dfs(i, now):
        nonlocal result
        if i == len(numbers):
            if now == target:
                result += 1
            return 
        
        dfs(i+1, now + numbers[i])
        dfs(i+1, now - numbers[i])
        
    dfs(0, 0)
    return result