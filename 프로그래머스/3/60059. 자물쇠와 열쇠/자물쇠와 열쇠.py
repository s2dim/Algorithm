def solution(key, lock):
    m = len(key)
    n = len(lock)
    x = n + (2 * (m - 1))
    
    arr = [[2] * (x) for i in range(x)]
    
    zero = 0
    
    for i in range(n):
        for j in range(n):
            arr[i+m-1][j+m-1] = lock[i][j]
            if lock[i][j] == 0:
                zero += 1
        
        rotate = key
    for d in range(4):
        rotate = list(map(list, zip(*rotate[::-1])))
        for w in range(x-m+1):
            for h in range(x-m+1):
                cnt = 0
                for i in range(m):
                    for j in range(m):
                        if rotate[i][j] == 0 and arr[i+w][j+h] != 0:
                            continue
                        elif rotate[i][j] == 1 and arr[i+w][j+h] != 1:
                            if arr[i+w][j+h] == 0:
                                cnt += 1
                            continue
                        else:
                            break

                if zero == cnt:
                    return True


    return False

'''
m < n
n의 상하좌우를 n-1 만큼 확장
4방향 전수조사

0은 2거나 1 이어야 함 -> 0이면 안 됨
1은 0이거나 2어야 함 -> 1이면 안 됨
zero가 0이 되면 성공

'''