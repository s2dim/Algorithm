import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
    try:
        a = sys.stdin.readline().split()

        if a[0] == 'push_front':
            deq.appendleft(a[1])

        elif a[0] == 'push_back':
            deq.append(a[1])
        
        elif a[0] == 'pop_front':
            b = deq.popleft()
            print(b)

        elif a[0] == 'pop_back':
            b = deq.pop()
            print(b)

        elif a[0] == 'size':
            print(len(deq))

        elif a[0] == 'empty':
            if deq:
                print(0)
            else:
                print(1)

        elif a[0] == 'front':
            print(deq[0])
        
        elif a[0] == 'back':
            print(deq[-1])
    
    except:
        print('-1')
        continue
