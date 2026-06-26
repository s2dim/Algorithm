from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = len(people) - 1
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            start += 1
        answer += 1
        
            
    
    return answer


'''
최대 2명
구명보트를 최대한 적게 사용

'''