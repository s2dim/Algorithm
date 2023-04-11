n = int(input())
lst = []
max_n = (n // 3) + 1
for i in range(0, max_n):
    for j in range(0, max_n):
        if 5 * i + 3 * j == n:
            lst.append(i + j)

if lst:
    print(min(lst))
else:
    print(-1)