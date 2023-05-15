def solution(sizes):
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i].reverse()
            
    a = [list(x) for x in zip(*sizes)]
    w = max(a[0])
    h = max(a[1])
    answer = w * h
    
    return answer