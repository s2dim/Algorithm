
from collections import Counter, deque

cnt = 0
n = int(input())
color = input()

lst = []
now = color[0]

for i in range(n+1):
    if i == n:
        lst.append((now, cnt))
        break

    if now == color[i]:
        cnt += 1
        continue

    else:
        lst.append((now, cnt))
        now = color[i]
        cnt = 1

r = color.count('R')
b = color.count('B')

left_r = 0
if lst[0][0] == 'R':
    left_r = lst[0][1]

right_r = 0
if lst[-1][0] == 'R':
    right_r = lst[-1][1]

left_b = 0
if lst[0][0] == 'B':
    left_b = lst[0][1]

right_b = 0
if lst[-1][0] == 'B':
    rifht_b = lst[-1][1]

print(min(r - left_r, r - right_r, b - left_b, b - left_b))