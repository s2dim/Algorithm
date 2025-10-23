import sys

n = int(sys.stdin.readline())
narr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
marr = list(map(int, sys.stdin.readline().split()))


narr.sort()

def binary(arr, x, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for i in marr:
    print(binary(narr, i, 0, n-1))