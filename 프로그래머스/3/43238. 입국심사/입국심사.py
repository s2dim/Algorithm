def solution(n, times):
    
    start = 1
    end = min(times) * n
    
    
    while start <= end:
        mid = (start + end) // 2
        
        total = sum([mid // t for t in times])
        
        if total >= n:
            end = mid - 1
        else:
            start = mid + 1

    return start
'''
모든 사람이 심사에 걸리는 최소 시간

입국심사 인원 n
심사관이 한 명 당 걸리는 시간 times

- 비어있는 심사대로 가서 받기 가능
- 더 빨리 끝나는 심사대 있으면 기다렸다 가기 가능

1. times 짧은 곳으로 먼저
2. 비교해서 더 빨리 끝나는 곳
-> 남은 시간 vs 걸리는 시간 비교 필요

- left 기준 min 에 넣기
- min이 같다면 인덱스 순서로


'''


