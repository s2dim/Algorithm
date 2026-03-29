import sys

n = int(input()) # oil 개수
distance = list(map(int, sys.stdin.readline().split())) # 필요 기름
oil = list(map(int, sys.stdin.readline().split())) # 주유소 가격

cost = 0
cheap = oil[0]

for i in range(n-1):
    cheap = min(cheap, oil[i])
    cost += cheap * distance[i]
print(cost)