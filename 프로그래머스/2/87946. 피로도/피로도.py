import itertools

def solution(k, dungeons):
    
    lst = list(itertools.permutations(dungeons, len(dungeons)))

    answer = 0
    for i in range(len(lst)):
        temp = k
        cnt = 0
        for j in range(len(dungeons)):
            if temp >= lst[i][j][0]:
                temp -= lst[i][j][1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer

'''
최소피로도 : 시작 필요조건
소모 피로도 : 마쳤을 때 소모됨

던전을 최대한 많이 돌려고 함
탐험할 수 있는 최대 던전 수 return 
던전 순서는 마음대로

고민해야 할 점
최대 피로도가 큰 거 먼저?
소모 피로도가 작은 것 먼저?
피로도 큰 것 먼저, 

던전이 8개이므로 완탐 가능할 듯!

'''