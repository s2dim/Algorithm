import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
x = int(input())

lst.sort()

start = 0
end = n - 1
cnt = 0

while start < end:
    if lst[start] + lst[end] == x:
        cnt += 1
        start += 1
        end -= 1
    if lst[start] + lst[end] > x:
        end -= 1
    elif lst[start] + lst[end] < x:
        start += 1

print(cnt)