from collections import defaultdict

def solution(id_list, report, k):
    dic = defaultdict(list)
    for i in report:
        a, b = i.split()
        dic[b].append(a)
        

    result = {i:0 for i in id_list}
    
    for key, value in dic.items():
        if len(set(value)) >= k:
            for i in set(value):
                result[i] += 1
                
    return list(result.values())

'''
한 유저 -> 동일 유저 : 1회
k번 이상 신고시 게시판 이ㅛㅇ 정지

'''