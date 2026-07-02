from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    stay = {}
    fee = defaultdict(int)
    
    # 텍스트 파싱
    for record in records:
        time, number, state = record.split()
        hour, minute = map(int, time.split(':'))
        
        if state == 'IN':
            stay[number] = (hour, minute)
        if state == 'OUT':
            # 머문 시간 계산
            inhour, inminute = stay[number]
            temp = (hour * 60) + minute - ((inhour * 60) + inminute)
            fee[number] += temp
            stay[number] = (-1, -1)
    
    
    for key, value in stay.items():
        if value != (-1, -1):
            inhour, inminute = value
            fee[key] += (23 * 60) + 59 - ((inhour * 60) + inminute)
    temp2 = sorted(fee.items())
    for i in temp2:  # fees = [기본 시간(분), 기본 요금, 단위 시간(분), 단위 요금]
        number = i[0]
        time = i[1]
        
        if time <= fees[0]:
            answer.append(fees[1])
        
        else:
            cal1 = time - fees[0]
            cal2 = math.ceil(cal1 / fees[2])
            answer.append(fees[1] + (cal2 * fees[3]))
        
    
    return answer

'''
- 출차 내역이 없다면 23:59 출차
- 차랑별 누적 주차 시간
    1) 기본 시간 이하 : 기본 요금
    2) 기본 시간 초과 : 기본 요금 + 초과 시간 * 단위 요금
        초과분에 대해서는 올림

- 차량 번호가 작은 자동차부터 출력

'''