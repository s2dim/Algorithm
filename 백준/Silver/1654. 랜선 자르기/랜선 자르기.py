import sys
k, n = map(int, sys.stdin.readline().split())

lan = []

for i in range(k):
    lan.append(int(input()))

start = 1
end = sum(lan) // n

while start <= end:
    mid = (start + end) // 2

    total = sum([l // mid for l in lan])

    if total < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)