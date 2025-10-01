import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    cnt = 0
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        
        if first >= K: # 최소가 K보다 크면 종료
            break
        
        second = heapq.heappop(scoville)

        if first == 0 and second == 0:
            cnt = -1
            break

        new = first + (second * 2)
        cnt += 1
        heapq.heappush(scoville, new)

                
    if len(scoville) == 1:
        last = heapq.heappop(scoville)
        if last <= K:
            cnt = -1
    
    answer = cnt
    return answer



'''
-1 이 return 하는 경우
1) 계속 더해도 k를 안 넘을 경우 [0, 0, 0, 1, 1]
2) [1, 2, 3] 100
'''