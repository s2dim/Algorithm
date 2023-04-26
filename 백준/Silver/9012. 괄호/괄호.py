import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline()

    while True:
        if '()' in a:
            a = a.replace('()', '')

        elif len(a) == 1:
            print("YES")
            break

        else:
            print("NO")
            break





        