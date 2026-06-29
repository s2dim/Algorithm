from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    check = deque([i for i in range(len(prices))])

    while check:
        q = check.popleft()
        cnt = 0
        for i in range(q+1, len(prices)):
            if prices[q] <= prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer[q] += cnt
        
    return answer