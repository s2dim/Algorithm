def solution(number, k):
    answer = []
    
    for now in number:
        while answer and k > 0 and answer[-1] < now:
            answer.pop()
            k -= 1
        
        answer.append(now)
    
    if k > 0:
        answer = answer[:-k]
    
    return ''.join(answer)
'''
가장 큰 수 찾아냄
k개 지워서 닿을 수 있는지 판단
이후 k:에서 작은 수부터 지우기
중복이 있을 경우엔 어떡하지

1 9 2 4
0 1 2 3
'''