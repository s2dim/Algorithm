a = input()
lst = a.split()
lst = list(map(int, lst))
lst.sort()

set_lst = set(lst)

if len(set_lst) == 1:
    award = 10000 + lst[0] * 1000
elif len(set_lst) == 3:
    award = max(lst) * 100
else:
    award = 1000 + lst[1] * 100

print(award)