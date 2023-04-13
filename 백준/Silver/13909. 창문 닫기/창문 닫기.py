import sys

n = int(sys.stdin.readline())

i = 1
cnt = 0

while i * i <= n:
    i += 1
    cnt += 1

print(cnt)