import sys
n = map(int, sys.stdin.readline())


a = sys.stdin.readline().split()
lst = [int(i) for i in a]

cnt = 0
for i in lst:
    num = [j for j in range(1, i+1) if i % j == 0]
    if len(num) == 2:
        cnt += 1

print(cnt)

