from collections import deque

def solution(numbers, target): # 부호 len(numbers)개

    cnt = 0
    
    def dfs(i, a):
        nonlocal cnt
        if i == len(numbers):
            if a == target:
                cnt += 1
            return
        
        dfs(i+1, a + numbers[i])
        dfs(i+1, a - numbers[i])
    
    dfs(0, 0)
    return cnt

'''
numbers 각 인덱스 별로 더하거나 빼기

'''