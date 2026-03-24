from collections import Counter

def solution(genres, plays):
    
    answer = []
    gen = {i:0 for i in genres}
    temp_cnt = dict(Counter(genres))
    
    for i in range(len(plays)):
        gen[genres[i]] += plays[i]
    
    sorted_gen = sorted(gen, key = lambda x:gen[x], reverse=True)
    
    for i in sorted_gen:
        temp = {}
        for j in range(len(genres)):
            if genres[j] == i:
                temp[j] = plays[j]
        sorted_temp = sorted(temp.items(), key = lambda x:(x[1], -x[0]), reverse=True)
        
        for k, v in sorted_temp[:2]:
            answer.append(k)
    return answer

'''
장르 별로 가장 많이 재생된 노래 2개씩 모아 출시
- 장르별 노래 재생 횟수 개산
- 장르 내에서 가장 많이 재생된 노래 수록 (재생 횟수가 같다면 고유 번호가 낮은 노래 먼저)

genres 먼저 count, 정렬
각 장르별 재생 횟수 계산
'''