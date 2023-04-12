import sys
import math

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

h = a * d + b * c
t = b * d

g = math.gcd(h, t)

h = h / g
t = t / g

print(int(h), int(t))