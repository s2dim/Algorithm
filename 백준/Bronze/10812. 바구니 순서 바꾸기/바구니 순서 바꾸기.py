import sys
a, b = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, a+1)]

for i in range(b):
    x, y, z = map(int, sys.stdin.readline().split())
    
    x = x - 1
    z = z - 1

    lst = lst[:x] + lst[z:y] + lst[x:z] + lst[y:] 

print(*lst)