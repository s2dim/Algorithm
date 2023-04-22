from collections import deque
import sys

n = int(sys.stdin.readline())

deq = deque()

for i in range(n):
    try:
        a = sys.stdin.readline().split()

        if a[0] == "push":
            deq.append(a[1])

        elif a[0] == "pop":
            print(deq[0])
            deq.popleft()


        elif a[0] == "size":
            print(len(deq))
        
        elif a[0] == "empty":
            if deq:
                print("0")
            else:
                print("1")

        elif a[0] == "front":
            print(deq[0])

        elif a[0] == "back":
            print(deq[-1])
    except:
        print("-1")
        pass

