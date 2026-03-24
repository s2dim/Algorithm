from collections import Counter

def solution(nums):
    
    n = len(nums) // 2
    dic = Counter(nums)
    
    cnt = len(dic.keys())
    
    answer = min(n, cnt)
    return answer