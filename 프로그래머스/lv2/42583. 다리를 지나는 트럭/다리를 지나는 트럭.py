def solution(bridge_length, weight, truck_weights):

    a = [0] * bridge_length
    sec = 0
    current_weights = 0
    while a:
        sec += 1
        current_weights -= a.pop(0)
        if truck_weights:
            if current_weights + truck_weights[0] <= weight:
                current_weights += truck_weights[0]
                a.append(truck_weights.pop(0))
            else:
                a.append(0)
    return sec