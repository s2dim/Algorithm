import sys
from collections import deque

n, d, k, c = map(int, sys.stdin.readline().split())

sushi = []

for i in range(n):
    num = int(input())
    sushi.append(num)

idx = [0] * (d+1)

idx[c] += 1
cnt = 1

for i in sushi[:k]:
    if idx[i] == 0:
        cnt += 1
    idx[i] += 1

max_ = cnt

for i in range(n):
    # 첫 번째 요소 삭제
    idx[sushi[i]] -= 1
    if idx[sushi[i]] == 0:
        cnt -= 1
    # 마지막 요소 추가
    new = sushi[(i+k) % n]
    if idx[new] == 0:
        cnt += 1
    idx[new] += 1

    max_ = max(max_, cnt)

print(max_)

'''
- 한 위치부터 연속 k개를 먹을 경우 할인
- 쿠폰 중 하나 무료 제공, 현재 벨트에 없으면 만들어 줌

'''