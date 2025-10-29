def solution(A, B):
    
    A.sort()
    B.sort()

    aidx = 0
    bidx = 0
    cnt = 0
    n = len(A)

    
    while aidx < n and bidx < n:
        if A[aidx] < B[bidx]:
            aidx += 1
            bidx += 1
            cnt += 1
        else:
            bidx += 1


    return cnt

    
'''
- 모든 사원 무작위 자연수
- 수가 큰 쪽이 승리 (+1점)
- 같으면 승점 ㄴㄴ

배열 A : 출전 순서대로 나열
B : 

큰 것 개수

1  3  5  7  | 3  3  2   2   1   1   0
2  2  6  8  | 4  3  3   2   2   1   1

'''