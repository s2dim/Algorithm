import sys

a, b = map(int, sys.stdin.readline().split())


a_lst = [a // i for i in range(1, a+1) if a % i == 0]
b_lst = [b // i for i in range(1, b+1) if b % i == 0]

s1 = set(a_lst)
s2 = set(b_lst)
s = s1 & s2

max_n = max(s)

result = max_n * (a // max_n) * (b // max_n)

print(int(result))