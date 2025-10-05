def solution(citations):
    n = len(citations)

    answer = 0
    
    citations.sort()
    
    left, right = 0, n - 1
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        h = n - mid
        
        if citations[mid] >= h:
            answer = h
            right = mid - 1
        else:
            left = mid + 1
    return answer

    
'''
인용횟수 = citations

n = len(citations)
h번 이상 인용이 >= h
나머지 <= h
h 최댓값 = h-index

0 1 3 5 6


'''