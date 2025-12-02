def solution(n, s):
    a = s // n
    b = s % n

    if s < n:
        return [-1]
    
    lst = [a for _ in range(n)]
    temp = b // n
    
    for i in range(n):
        lst[i] += temp
    
    for i in range(b % n):
        lst[n-1-i] += 1
    
    return lst