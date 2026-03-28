import sys

n = int(input())
oil = list(map(int, sys.stdin.readline().split())) # 필요 기름
bank = list(map(int, sys.stdin.readline().split())) # 주유소 가격

idx = 0
cost = 0

while idx < n-1:

    for i in range(idx + 1, n):
        if bank[idx] >= bank[i]:
            cost += sum(oil[idx:i]) * bank[idx]
            idx = i
            break
    
print(cost)