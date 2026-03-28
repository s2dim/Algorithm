import sys

n = int(input()) # bank의 개수
oil = list(map(int, sys.stdin.readline().split())) # 필요 기름
bank = list(map(int, sys.stdin.readline().split())) # 주유소 가격

idx = 0 # bank에 대한 idx
cost = 0

while idx < n-1:

    for i in range(idx + 1, n):
        if bank[idx] >= bank[i]:
            cost += sum(oil[idx:i]) * bank[idx]
            idx = i
            break

if cost == 0:
    cost = sum(oil) * bank[idx]
print(cost)