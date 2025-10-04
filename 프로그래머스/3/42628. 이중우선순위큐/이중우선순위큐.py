import heapq

def solution(operations):
    
    def cal(x, hq):
        if x[0] == 'I':
            heapq.heappush(hq, int(x[2:]))
        else:
            if x[2] != '-' and hq:
                temp = []
                
                for i in hq:
                    heapq.heappush(temp, -i)
                heapq.heappop(temp)
                hq = []
                
                for i in temp:
                    heapq.heappush(hq, -i)
                    
            elif x[2] == '-' and hq:
                heapq.heappop(hq)
        return hq
    
    hq = []
    for i in range(len(operations)):
        hq = cal(operations[i], hq)
    
    if hq:
        answer = [max(hq), min(hq)]
    else:
        answer = [0, 0]

    return answer


'''
첫 글자가 I or D
I라면 공백 뒤 숫자
D라면 공백 뒤 1 or -1


'''