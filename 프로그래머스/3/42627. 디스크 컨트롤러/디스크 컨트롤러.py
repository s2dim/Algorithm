import heapq

def solution(jobs):
    n = len(jobs) # 요청 개수
    time = 0 # 현재 시간
    tt = 0 # 반환 시간
    cnt = 0
    
    heapq.heapify(jobs)
    h = []


    while cnt < n: # 최대 n번 반복
        
        while jobs and jobs[0][0] <= time:
            
            a = heapq.heappop(jobs)
            heapq.heappush(h, (a[1], a))
                     
        if h:
            heapq.heapify(h)
            
            _, row = heapq.heappop(h)
            cnt += 1
            request, worktime = row

            time += worktime
            tt += (time - request)
            
        else:
            time += 1
            
    
    answer = tt // n
    return answer

'''
작업 마칠 때까지 하나만 수행


하드 작업 ㄴ 대기큐 ㅇ
1. 우선순위 순서
소요시간 짧음 > 요청 시각 빠름 > 작업 번호가 작음

[요청 시점, 소요시간]
반환 시간 = 작업 마친 시간 - 요청시간

!! 고민해야 할 점
1. 작업번호는 요청시각 순인가? -> 일단 그렇다고 가정하고 풀이
2. jobs는 어떤 기준으로 정렬되어 주어지는가? -> 일단 정렬 한 번 해 주자


요청 시점에 존재하는 작업이어야 함
- 현재 시간보다 요청 시점이 작은 리스트 뽑음
- 소요시간 순 정렬
- 마치면 다시 리스트 뽑음
- 소요시간 순 정렬



'''