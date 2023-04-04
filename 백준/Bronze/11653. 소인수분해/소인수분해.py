n = int(input())

lst = [i for i in range(1, n+1) if n % i == 0]
lst = lst[1:]
# new_2 = [i for i in lst if i % 2 != 0 and i % 3 != 0]
# # new_3 = [i for i in lst if i % 3 != 0]
# # print(new_2)

for i in lst:
    while n % i == 0:
        n = n // i
        print(i)
    
