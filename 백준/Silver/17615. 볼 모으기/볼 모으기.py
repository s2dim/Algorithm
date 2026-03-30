import sys

n = int(sys.stdin.readline())
color = list(map(str, sys.stdin.readline().strip()))

min_ = int(1e9)
cnt = 0
temp = 0

#오른쪽 보내기
for i in range(n):
    if color[i] == 'R':
        temp += 1
    if color[i] == 'B' and temp:
        cnt += temp
        temp = 0

min_ = min(min_, cnt)

cnt = 0
temp = 0
color.reverse()
for i in range(n):
    if color[i] == 'R':
        temp += 1
    if color[i] == 'B' and temp:
        cnt += temp
        temp = 0

min_ = min(min_, cnt)

cnt = 0
temp = 0
for i in range(n):
    if color[i] == 'B':
        temp += 1
    if color[i] == 'R' and temp:
        cnt += temp
        temp = 0
min_ = min(min_, cnt)

color.reverse()
cnt = 0
temp = 0
for i in range(n):
    if color[i] == 'B':
        temp += 1
    if color[i] == 'R' and temp:
        cnt += temp
        temp = 0
min_ = min(min_, cnt)

print(min_)