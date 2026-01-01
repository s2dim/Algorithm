from collections import deque

def solution(progresses, speeds):
    waiting = deque([])
    answer = []
    
    for i in range(len(progresses)):
        nam = 100 - progresses[i]
        day = nam // speeds[i]
        if nam % speeds[i] != 0:
            day += 1
        waiting.append(day)
           
    print(waiting)
    now = waiting.popleft()
    cnt = 1
    
    while waiting:
        if waiting[0] <= now:
            waiting.popleft()
            cnt += 1
        else:
            if cnt != 0:
                answer.append(cnt)
            cnt = 1
            now = waiting.popleft()
    
    answer.append(cnt)
    
    return answer

'''
- 진도가 100% 일 때 반영 가능
- 뒤에 있는 기능이 먼저 개발될 수 있음 -> 앞 기능이 배포될 때 함께 배포
- 배포는 하루에 한 번

- 대기 목록 생성
- 100% 차면 인덱스 삽입
now 인덱스보다 큰 애들 함께 배포
'''