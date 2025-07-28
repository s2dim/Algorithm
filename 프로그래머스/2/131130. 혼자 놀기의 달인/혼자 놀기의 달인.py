def DFS(arr, visited, n, box):
    stack = []
    stack.append(box)
    cnt = 0
    
    while stack:
        a = stack.pop()
        cnt += 1
        
        if not visited[a]:
            visited[a] = True

        for i in range(1, (n+1)):
            if arr[a][i] == 1 and not visited[i]:
                stack.append(i)
    return cnt, visited

def solution(cards):
    
    n = len(cards)
    arr = [[0] * (n+1) for i in range((n+1))]
    
    # n번 상자에 숫자 카드 삽입
    for i in range(1, (n+1)):
        arr[i][cards[i-1]] = 1
    
    # n개의 방문 배열
    visited = [False] * (n+1)
    answer = 1
    answer_list = []
    
    for i in range(1, (n+1)):
        if not visited[i]:
            cnt, visited = DFS(arr, visited, n, i)
            answer_list.append(cnt)
            

    answer_list.sort(reverse=True)
    if answer_list[0] == n:
        answer = 0
    else:
        answer = answer_list[0] * answer_list[1]
    
    
            
    return answer