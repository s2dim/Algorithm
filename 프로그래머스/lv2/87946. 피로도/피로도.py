from itertools import permutations
import copy

def solution(k, dungeons):
    
    lst = list(permutations(dungeons, len(dungeons)))
    
    score = []
    origin_k = copy.deepcopy(k)

    for i in range(len(lst)):
        cnt = 0
        k = origin_k

        for j in range(len(dungeons)):
            if k >= lst[i][j][0]:
                k = k - lst[i][j][1]
                cnt += 1

        score.append(cnt)
    
    return max(score)
