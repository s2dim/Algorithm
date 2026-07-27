def solution(targets):
    sorting = sorted(targets, key = lambda x : x[1])

    last = 0
    answer = 0
    
    for start, end in sorting:
        if start >= last:
            answer += 1
            last = end
            
    return answer

'''
1) 한 줄로 나열
2) 가장 많은 지점부터 발사 (개구간?)
3) 삭제

리스트 만든다 -> 범위가 너무 크다
인덱스 삽입

'''