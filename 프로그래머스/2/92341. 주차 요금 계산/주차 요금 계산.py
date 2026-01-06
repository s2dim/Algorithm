import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    dic = {}
    cost = defaultdict(int)

    def cal(time):
        fee = 0
        if time <= fees[0]:
            fee += fees[1]
        else:
            fee += fees[1]
            extra = time - fees[0]
            extra = math.ceil(extra / fees[2])
            fee += extra * fees[3]
        return fee
            
    for i in records:
        lst = i.split(' ')
        hour, minute = map(int, lst[0].split(":"))
        time = (hour * 60) + minute
        number = lst[1]
        state = lst[2]
        
        num_lst = list(cost.keys())


        if state == 'IN':
            dic[number] = time
            
        elif state == 'OUT':
            cost[number] += time - dic.get(number)
            dic.pop(number)

    for key, value in dic.items():
        cost[key] += ((23 * 60) + 59) - value
        
    for key, value in cost.items():
        cost[key] = cal(value)
    
    cost_lst = sorted(cost.items())
    
        
    
    
    return [value for key, value in cost_lst]


'''
- 출차 내역이 없다면 23:59 출차
- 누적 주차 시작이 기본 이하 -> 기본 요금 청구
- 기본 시간 초과 -> 기본 요금 + 추가요금 (초과 단위시간(올림) * 단위 요금)
- 차량번호가 작은 자동차부터 주차 요금 담아 완성

fees [기본 시간(분), 기본 요금, 단위 시간, 단위 요금]

{key:{(in, out)}}
'''