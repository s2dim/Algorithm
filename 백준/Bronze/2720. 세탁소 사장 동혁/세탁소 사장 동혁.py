num = int(input())

lst = []

for i in range(num):
    a = int(input()) 

    q = 0
    d = 0
    n = 0
    p = 0

    if a / 25 >= 1:
        q = a // 25
        a = a % 25

    if a / 10 >= 1:
        d = a // 10
        a = a % 10

    if a / 5 >= 1:
        n = a // 5
        a = a % 5

    p = a // 1

    pay = [int(q), int(d), int(n), int(p)]
    lst.append(pay)

for i in lst:
    print(*i)