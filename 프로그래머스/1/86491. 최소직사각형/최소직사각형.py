def solution(sizes):
    
    big = []
    small = []
    
    
    for i in range(len(sizes)):
        big.append(max(sizes[i][0], sizes[i][1]))
        small.append(min(sizes[i][0], sizes[i][1]))
            

    answer = max(big) * max(small)
    return answer