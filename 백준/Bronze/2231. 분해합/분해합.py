a = int(input())

n = 0
for i in range(1, a+1):
    b = list(map(int, str(i)))
    n = i + sum(b)
    if n == a:
        print(i)
        break

    if i == a:
        print(0)
