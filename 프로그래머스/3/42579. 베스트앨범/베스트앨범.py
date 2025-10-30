from collections import defaultdict
def solution(genres, plays):
    
    genre = set(genres)
    
    dic = defaultdict(int)
    
    for i in range(len(genres)):
        dic[genres[i]] += plays[i]
    
    dic = dict(sorted(dic.items(), key = lambda item :item[1], reverse=True))
    
    # 많이 들은 순으로 정렬
    idx_dic = {}
    key = list(dic.keys())
    for i in range(len(key)):
        idx_dic[key[i]] = i

    song = defaultdict(list)

    for i in range(len(genres)):
        song[i].append((idx_dic.get(genres[i]), plays[i]))
    
    song = sorted(song.items(), key = lambda item : (item[1][0][0], -item[1][0][1], item[0]))
    
    answer = []
    
    before = None
    cnt = 1

    for i in song:
        if i[1][0][0] == before:
            if cnt < 2:
                answer.append(i[0])

            cnt += 1
            
        elif i[1][0][0] != before:
            answer.append(i[0])
            before = i[1][0][0]
            cnt = 1
            
                
    return answer


'''
많이 재생된 장르 (두 개씩) > 장르 내에서 많이 재생된 노래 > 고유번호가 낮은 노래

고유번호별로 : 장르, plays

1. 장르별로 plays 더함
2. 장르 -> plays -> 고유번호 순으로 나열

장르 구분-> enumerate
(장르, pays, 고유번호 순 삽입)


'''