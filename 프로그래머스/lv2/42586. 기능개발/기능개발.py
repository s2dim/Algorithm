import math

def solution(progresses, speeds):
    cnt = len(progresses)
    
    def cnt_day(progress, speed):
        day = math.ceil((100 - progress) / speed)

        return day
    
    lst = [cnt_day(progresses[i], speeds[i]) for i in range(cnt)] 
    new = []
    
    num = 1
    
    maxe = lst.pop(0)
    
    while True:
        if len(lst) >= 1:
            temp = lst.pop(0)
            if maxe >= temp:
                num += 1

                
            else:
                maxe = temp
                new.append(num)
                num = 1
                # lst.pop(0)

        else:
            new.append(num)
            break
                

    answer = new
    return answer