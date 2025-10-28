def solution(s):
    
    n = len(s)
    min_ = len(s)
    if n == 1:
        return 1

    for step in range(1, n // 2 + 1):
        prev = s[:step]
        cnt = 1
        out = []
        
        for i in range(step, n, step):
            if prev == s[i:step+i]:
                cnt += 1
            else:
                if cnt > 1:
                    out.append(str(cnt))
                out.append(prev)
                cnt = 1
                prev = s[i:step+i]
                
        if cnt > 1:
            out.append(str(cnt))
        out.append(prev)
        answer = ''.join(out)
        
        min_ = min(min_, len(answer))
    return min_