import sys
import math

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)

distance = []
for i in range(len(lst) - 1):
    b = lst[i+1] - lst[i]
    distance.append(b)

g = math.gcd(distance[0], distance[1])
for i in range(2, len(distance) - 1):
    g = math.gcd(g, distance[i+1])

result = (lst[-1] - lst[0]) / g

print(int(result - len(lst) + 1))