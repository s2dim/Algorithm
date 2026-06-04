from collections import deque

def solution(plans):
    waiting = []
    time = []
    answer = []
    idx = 0
    
    # 시간 순 정렬
    new = deque(sorted(plans, key = lambda x:x[1]))
    
    # time 리스트 생성
    for i in range(1, len(new)):
        minute2 = int(new[i][1][:2]) * 60 + int(new[i][1][-2:])
        minute1 = int(new[i-1][1][:2]) * 60 + int(new[i-1][1][-2:])
        time.append(minute2 - minute1)
    
    
    def action(sub, now, left, idx):
        if now < left:
            waiting.append((sub, left - now))
            return idx + 1
        elif now == left:
            answer.append(sub)
            return idx + 1
        elif now > left:
            answer.append(sub)
            if waiting:
                temp, w = waiting.pop()
                return action(temp, now - left, w, idx)
            else:
                return idx + 1

                
            
    while new:
        if idx < len(time):
            temp = new.popleft()
            sub = temp[0]
            left = int(temp[2])
            now = time[idx]
            idx = action(sub, now, left, idx)
            
        else:
            temp = new.popleft()
            answer.append(temp[0])
            
    while waiting:
        answer.append(waiting.pop()[0])

    return answer

'''
새로운 과제 시간이 되면 진행 중이던 과제 멈춤
진행 중인 과제가 끝내면 멈춘 과제 이어서 (최근 순)
과제를 끝낸 순서대로 배열에 담아 출력

시간 차이 리스트 time = [0, 30, 20]
time = [40, 80, ]

'''