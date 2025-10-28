import sys

n = list(map(int, sys.stdin.readline().rstrip()))

mid = (len(n) // 2)

left = n[:mid]
right = n[mid:]

if (sum(left) == sum(right)):
    print("LUCKY")
else:
    print("READY")