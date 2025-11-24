import math

def solution(storey):
    storey = storey
    n = 0
    left = 0

    while storey > 0:
        left = storey % 10
        storey = storey // 10

        if left > 5:
            n += (10 - left)
            storey += 1
        elif left < 5:
            n += left
        else: 
            if storey % 10 >= 5:
                n += 5
                storey += 1
            else:
                n += 5


    return n