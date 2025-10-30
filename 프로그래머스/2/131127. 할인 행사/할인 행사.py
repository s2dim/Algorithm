from collections import Counter

def solution(want, number, discount):
    lst = dict(zip(want, number))
    lst = dict(sorted(lst.items(), key = lambda x:x[0]))

    
    n = 10
    
    answer = 0
    for i in range(0, len(discount)-(n-1)):
        buy = discount[i:i+n]
        cnt = dict(Counter(buy))
        cnt = dict(sorted(cnt.items(), key = lambda x:x[0]))
        
        if lst == cnt:
            answer += 1

    return answer


'''
- 매일 한 가지 할인
- 할인 제품은 매일 한 개만 구매 가능

'''