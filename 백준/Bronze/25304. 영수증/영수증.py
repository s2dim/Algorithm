total = int(input())
n = int(input())

lst = []
for i in range(n):
    a, b = map(int, input().split())
    lst.append(a * b)

if sum(lst) == total:
    print("Yes")
else:
    print("No")