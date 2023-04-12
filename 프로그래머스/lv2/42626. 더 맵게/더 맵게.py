import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K and len(scoville) > 1:
        min_ = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        new = (min_ + min_2 * 2)
        heapq.heappush(scoville, new)
        cnt += 1
    if scoville[0] >= K:
        return cnt

    else:
        return -1



            
'''

'''
