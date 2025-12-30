from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    time = 0
    
    now = deque([0] * bridge_length)
    heavy = 0
    
    while truck_weights:
        n = now.popleft()
        heavy -= n
        
        time += 1

        if heavy + truck_weights[0] <= weight:
            q = truck_weights.popleft()
            now.append(q)
            heavy += q
            
        else:
            now.append(0)
            
        
    while now and sum(now) > 0:
        now.popleft()
        time += 1
            
    return time

'''
bridge_length : 최대 올라갈 수 있는 개수
weight : 견디는 무게

nㅊ부터 하나씩 pop


'''