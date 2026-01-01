import sys

h, w = map(int, sys.stdin.readline().split())

block = list(map(int, sys.stdin.readline().split()))
arr = []

for i in block:
    lst = [1] * i + [0] * (h-i)
    arr.append(lst)

arr = list(map(list, zip(*arr[::-1])))

cnt = 0
for i in range(h):
    water = 0
    open = False
    if arr[i].count(1) > 1:
        for j in range(w):
            if arr[i][j] == 1: # 블럭을 만나는 경우
                if not open: # 닫혀 있으면 open
                    open = True
                else: # 열려있지만 닫히지 않은 경우
                    cnt += water # 물 담고 다시 cnt
                    water = 0
            elif arr[i][j] == 0 and open:
                water += 1
                
print(cnt)

