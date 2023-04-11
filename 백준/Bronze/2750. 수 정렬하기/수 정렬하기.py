n = int(input())

lst = []
for i in range(n):
    a = int(input())
    lst.append(a)

lst = list(set(lst))
lst.sort()

for i in lst:
    print(i)