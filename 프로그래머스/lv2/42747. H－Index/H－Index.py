def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
        
    return len(citations)

'''

0 1 3 5 6
2번 3개
3번 3개
4번 2개



'''