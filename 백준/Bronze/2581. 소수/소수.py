a = int(input())
b = int(input())

number = [i for i in range(a, b+1)]

lst = []
for i in number:
    new = [j for j in range(1, i+1) if i % j == 0]
    num = len(new)

    if num == 2:
        lst.append(new[1])

if lst:
    print(sum(lst))
    print(lst[0])

else:
    print(-1)