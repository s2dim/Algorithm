def minerals_cnt(min_group):
    dia_cnt = min_group[1] // 100 
    iron_cnt = (min_group[1] % 100) // 10
    stone_cnt = (((min_group[1] % 100) % 10) // 1)
    
    return (dia_cnt, iron_cnt, stone_cnt)


def solution(picks, minerals):
    
    minerals = minerals[0:5*sum(picks)]
    
    n = len(minerals)
    
    cnt = (n + 4) // 5 # 그룹 개수
    score = [] # 점수로 변환
    last = n-(5*(cnt-1)) # 마지막 그룹 요소 개수

    
    # 가중치로 변경
    for i in minerals:
        if i == "diamond":
            score.append(100)
        elif i == "iron":
            score.append(10)
        elif i == "stone":
            score.append(1)

    min_group = [0] * cnt
    
    for i in range((cnt-1)):
        min_group[i] = (5, sum(score[5*i:5*(i+1)]))
                        
    # 마지막 그룹 처리
    min_group[(cnt-1)] = (last, sum(score[5*(cnt-1):n]))
    
    min_group.sort(key=lambda x: x[1], reverse=True)
    
    dia, iron, stone = picks
    tired = 0
    
    for i in range(cnt):
        if dia > 0:
            dia -= 1
            tired += 1 * min_group[i][0]
        
        elif iron > 0:
            iron -= 1
            tired += 5 * minerals_cnt(min_group[i])[0]
            tired += 1 * minerals_cnt(min_group[i])[1]
            tired += 1 * minerals_cnt(min_group[i])[2]

        elif stone > 0:
            stone -= 1
            tired += 25 * minerals_cnt(min_group[i])[0]
            tired += 5 * minerals_cnt(min_group[i])[1]
            tired += 1 * minerals_cnt(min_group[i])[2]
                
        
        if dia == 0 and iron == 0 and stone == 0:
            break
                
    return tired