def solution(prices):
    
    answer = [0] * (len(prices))
    start = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if j != len(prices):
                answer[i] += 1
            if prices[i] <= prices[j]:
                continue
            else:
                break
    return answer