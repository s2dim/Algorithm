import sys

n = int(sys.stdin.readline())

arr =[[] for i in range(201)]
for i in range(n):
    a, b = sys.stdin.readline().split()
    a = int(a)
    arr[a].append(b)

for i in range(201):
    if arr[i]:
        if len(arr[i]) == 1:
            print(i, *arr[i])
        else:
            for j in arr[i]:
                print(i, j)

