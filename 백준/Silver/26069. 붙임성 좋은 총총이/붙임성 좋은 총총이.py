import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    a, b = sys.stdin.readline().split()
    
    if a in lst or b in lst:
        lst.append(a)
        lst.append(b)

    elif a == 'ChongChong' or b == 'ChongChong':
        lst.append(a)
        lst.append(b)

lst = set(lst)
print(len(lst))