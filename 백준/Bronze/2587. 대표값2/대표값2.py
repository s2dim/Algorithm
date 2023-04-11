lst = []
for i in range(5):
    n = int(input())
    lst.append(n)

lst.sort()
avg = sum(lst) / 5
mid = lst[2]

print(int(avg), mid)