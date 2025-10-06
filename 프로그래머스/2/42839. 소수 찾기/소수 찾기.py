import itertools
import math

def solution(numbers):
    num = list(numbers)
    
    lst = []
    
    # 순열 구현
    for i in range(2, len(numbers)+1):
        temp = list(itertools.permutations(num, i))
        for j in range(len(temp)):
            lst.append(temp[j])
        
    num_lst = list(numbers)
    for i in range(len(lst)):
        num_lst.append(''.join(lst[i]))
    
    num_lst = list(map(int, num_lst))
    num_lst = set(num_lst)

    for i in (0, 1):
        if i in num_lst:
            num_lst.remove(i)
 
    # 소수 판별
    def prime(n):
        end = int(math.sqrt(n))
        
        for i in range(2, end+1):
            if n % i == 0:
                return False
        return True
    
    answer = 0
    
    for i in num_lst:
        if prime(i):
            answer += 1
    
    return answer

'''
1. 숫자 만들기
2. 소수 판별
'''