def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    # 이기면 1 지면 2
    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = 2
    
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == 1 and graph[k][b] == 1 and a != b:
                    graph[a][b] = 1
                    graph[b][a] = 2
                elif graph[a][k] == 2 and graph[k][b] == 2 and a != b:
                    graph[b][a] = 1
                    graph[a][b] = 2

    # a < k   k < b
    # a > k  k > b   a > b
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 0 and i != j:
                cnt += 1
                break
    
    return n - cnt
