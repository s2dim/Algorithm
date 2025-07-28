def solution(X, Y):
    x_list = [0] * 10
    y_list = [0] * 10
    
    for i in range(len(X)):
        n = int(X[i])
        x_list[n] += 1
        
    for i in range(len(Y)):
        n = int(Y[i])
        y_list[n] += 1
        
    ans_list = []
    
    for i in range(10):
        if x_list[i] >= 1 and y_list[i] >= 1:
            min_ = min(x_list[i], y_list[i])
            for j in range(min_):
                ans_list.append(i)
    
    if ans_list:
        if sum(ans_list) == 0:
            answer = "0"
        else:
            ans_list.sort(reverse=True)
            answer = ''.join(map(str, ans_list))
    
    else:
        answer = "-1"
    
    return answer