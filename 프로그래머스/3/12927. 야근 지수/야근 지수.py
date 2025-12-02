import heapq

def solution(n, works):
    answer = 0
    
    # 초기 종료 조건
    if sum(works) <= n:
        return answer
    
    temp = [-i for i in works]
    heapq.heapify(temp)
    while n > 0:
    
        a = heapq.heappop(temp)

        a += 1 # 최솟값 (실제는 최대) pop
        
        if a > 0: # 최소가 양수일 경우 (실제는 음수) 종료
            a = 0
            heapq.heappush(temp, a)
            return answer
            
        heapq.heappush(temp, a)
        n -= 1
    answer = sum([i*i for i in temp])
    return answer

'''
야근 피로도 : 시작 시점 ~ 남은 일 작업량 제곱
n시간 동안 일하고 피로도 최소화



'''