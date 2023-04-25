import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    try:
        a = sys.stdin.readline().split()

        if a[0] == "push":
            lst.append(a[1])

        elif a[0] == "pop":
            b = lst.pop(-1)
            print(b)

        elif a[0] == "size":
            print(len(lst))
        
        elif a[0] == "empty":
            if lst:
                print("0")
            else:
                print("1")

        elif a[0] == "top":
            print(lst[-1])
    except:
        print("-1")