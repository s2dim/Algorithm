lst = input().split()
lst = [int(i) for i in lst]

max_n = max(lst)
lst.remove(max_n)
lst.sort()

if max_n >= sum(lst):
    max_n = sum(lst) - 1
    lst.append(max_n)
else:
    lst.append(max_n)
    
print(sum(lst))