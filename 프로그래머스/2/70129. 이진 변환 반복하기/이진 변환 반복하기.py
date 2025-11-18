from collections import Counter

def solution(s):
    
    n = len(s)
    cnt = 0 # 실행 횟수
    ans = 0 # 0 개수
    
    def transfer(s):
        lst = list(s)
        c = Counter(lst)
        zero = c["0"]
        s = bin(n - zero).lstrip('0b') # 문자
        return zero, s
    
    while s != '1':
        zero, s = transfer(s)
        n = len(s)
        cnt += 1
        ans += zero

    return [cnt, ans]


