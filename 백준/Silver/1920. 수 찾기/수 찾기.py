import sys
import math

sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
Narr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
Marr = list(map(int, sys.stdin.readline().split()))

Narr.sort()

def bs(arr, x, start, end):
    
    if start > end:
        print("0")
        return
    
    if start == end:
        if arr[start] == x:
            print("1")
        else:
            print("0")
        return

    else:
        mid = (start + end) // 2
        if x > arr[mid]:
            start = mid + 1
            # print(f"if_1 배열 : {arr} x : {x}, start : {start} end : {end}")
            bs(arr, x, start, end)

        elif x < arr[mid]:
            end = mid - 1
            # print(f"if_2 배열 : {arr} x : {x}, start : {start} end : {end}")
            bs(arr, x, start, end)
        elif x == arr[mid]:
            print("1")


for i in Marr:
    bs(Narr, i, 0, n - 1)
