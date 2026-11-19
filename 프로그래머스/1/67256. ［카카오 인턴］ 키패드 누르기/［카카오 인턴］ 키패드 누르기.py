def solution(numbers, hand):
    
    def middlecnt(now, mx):
        if now[0] == 1: # 가운데 열이면 그냥 빼기
            return abs(now[1] - mx)
        if now[1] == mx: 
            return abs(now[1] - mx) + 1
        else:
            return abs(now[1] - mx) + 1
    
    
    answer = ''
    
    nowl = [0, 3]
    nowr = [2, 3]
    
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 10, 0]]
    
    left = [1, 4, 7, 10]
    middle = [2, 5, 8, 11]
    right = [3, 6, 9, 12]
    
    tempx, tempy = nowl

    # print("test", arr[tempx][tempy])
    for i in numbers:
        print("now", "l", arr[nowl[1]][nowl[0]], "r", arr[nowr[1]][nowr[0]])
        if i == 0:
            i = 11
        
        if i in left:
            answer += 'L'
            nowl = [0, left.index(i)]
            
        elif i in right:
            answer += 'R'
            nowr = [2, right.index(i)]
            
        else: # 중간 자판 누를 때
            nowm = middle.index(i) # 몇 번째 라인
        
            absl = middlecnt(nowl, nowm) # 왼쪽 최소
            absr = middlecnt(nowr, nowm) # 오른쪽 최소
            # print("!!", absl, absr, "test", "nowl", nowl, "nowm", nowm)

            if absl > absr:
                answer += 'R'
                nowr = [1, nowm]
            elif absl < absr:
                answer += 'L'
                nowl = [1, nowm]   
            elif absl == absr:
                if hand == 'right':
                    answer += 'R'
                    nowr = [1, nowm]
                elif hand == 'left':
                    answer += 'L'
                    nowl = [1, nowm]
                    
        print(i, answer[-1])
    return answer


'''
시작지점 : 왼 * 오 #
1, 4, 7 -> 왼손
3, 6, 9 -> 오른손
2, 5, 8 0 -> 가까운 손 (거리가 같다면 왼오잡이)
'''