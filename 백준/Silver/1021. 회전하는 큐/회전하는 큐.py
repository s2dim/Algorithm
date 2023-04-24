import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
deq = deque([i+1 for i in range(n)])
b = sys.stdin.readline().split()
b = [int(i)-1 for i in b]

cnt = 0
origin = copy.deepcopy(deq)


for i in b:
    if deq[0] == origin[i]:
        deq.popleft()



    else:
        if deq.index(origin[i]) <= (len(deq) // 2):
            while deq[0] != origin[i]:
                # print("1!", deq.index(origin[i]), (len(deq) // 2))
                cnt += 1
                deq.append(deq.popleft())

            deq.popleft()


        else:
            while deq[0] != origin[i]:
                # print("2!", deq.index(origin[i]))
                cnt += 1
                deq.appendleft(deq.pop())

            deq.popleft()





print(cnt)