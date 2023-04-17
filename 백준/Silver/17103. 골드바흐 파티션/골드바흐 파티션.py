import sys

check = [True] * 1000001
check[0] = False
check[1] = False


for i in range(2, 1000001):
    if check[i]:
        for j in range(2*i, 1000001, i):
            check[j] = False

n = int(sys.stdin.readline())


for i in range(n):
    count = 0
    num = int(sys.stdin.readline())
    for j in range(2, num//2+1):
        if check[j] and check[num-j]:
            count += 1
    print(count)
