
from itertools import combinations
lst = []

for i in range(9):
    n = int(input())
    lst.append(n)

lst.sort()

new_sum = sum(lst)
ans = new_sum - 100

com_lst = list(combinations(lst, 2))

for i in com_lst:
    if sum(i) == ans:
        lst.remove(i[0])
        lst.remove(i[1])
        break

for i in lst:
    print(i)