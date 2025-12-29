import math

def solution(n):
    cnt = 1
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            n = n // 2
            cnt += 1

    
    return cnt


'''
- k칸 앞으로 점프 -> 건전지 사용량 k
- 현재 온 거리 x 2 -> 건전지 사용량 0

5000
2500
1250
625 - 1
624
312
106
53 - 1
52
26
13 -1 
12
6
3 - 1
2
1
5^4 * 2^3
2
'''