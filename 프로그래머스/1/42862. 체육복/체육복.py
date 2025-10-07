def solution(n, lost, reserve):
    visited = [False] * (n+2)
    lost.sort()
    reserve.sort()
    
    for i in reserve:
        visited[i] = True
    
    # 여별 가진 학생 중 도난 당했는지 확인
    for i in lost:
        if visited[i]:
            visited[i] = False

    lost = [i for i in lost if i not in reserve]
    
    answer = n - len(lost)
    
    for i in lost:
        if visited[i-1]:
            visited[i-1] = False
            answer += 1
            
        elif visited[i+1]:
            visited[i+1] = False
            answer += 1

    
    print(lost)
    return answer

'''
n : 전체 학생 수
lost : 도난 당한 학생 배열
reserve : 여별 체육복 가져온 학생

- 여별 체육복 가진 학생만 대여 가능
- 여별 체육복 가진 학생도 도난 가능

제대로 가져온 애들 = n - len(lost)

1. 빌려줄 수 있는지 체크 <- visited로 reseve 다 적음
- 본인 확인
+1, -1 확인
1번, n번 인덱스 조심!




'''

