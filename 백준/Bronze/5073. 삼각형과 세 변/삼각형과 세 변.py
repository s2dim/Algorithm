import sys

while True:
    lst = sys.stdin.readline().split()
    lst = [int(i) for i in lst]

    if lst == [0, 0, 0]:
        break
    set_lst = list(set(lst))
    max_n = max(lst)
    lst.remove(max_n)

    if max_n >= sum(lst):
        print("Invalid")

    elif len(set_lst) == 3:
        print("Scalene")
    elif len(set_lst) == 2:
        print("Isosceles")
    elif len(set_lst) == 1:
        print("Equilateral")

