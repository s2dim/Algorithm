
import sys

sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
Narr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
Marr = list(map(int, sys.stdin.readline().split()))

Narr.sort()

def bs(arr, x, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in Marr:
    print(bs(Narr, i, 0, n - 1))
