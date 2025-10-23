import sys

# n 나무 수 m 가져가려는 나무 길이
n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

max_h = max(height)

def bs(height, start, target, end):
    while start <= end:
        mid = (start + end) // 2
        sum_h = sum(x - mid for x in height if x > mid)

        if sum_h >= target:
            start = mid + 1
        else:
            end = mid - 1

    return end

ans = bs(height, 0, m, max_h)

print(ans)