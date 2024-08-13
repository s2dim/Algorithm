
import math

lst = [[0]*6, [0]*6]
room = 0
n, k = map(int, input().split())

for i in range(n):
    a, b = map(int, input().split())
    b = b - 1
    lst[a][b] += 1
    
for i in range(2):
    for j in range(6):
        if lst[i][j] != 0:

            room += math.ceil(lst[i][j] / k)


print(room)
    