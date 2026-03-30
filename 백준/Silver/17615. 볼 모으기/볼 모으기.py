n = int(input())
color = input()

# 전체 개수
total_r = color.count('R')
total_b = color.count('B')

# 왼쪽에서 연속된 R
left_r = 0
for c in color:
    if c == 'R':
        left_r += 1
    else:
        break

# 오른쪽에서 연속된 R
right_r = 0
for c in reversed(color):
    if c == 'R':
        right_r += 1
    else:
        break

# 왼쪽에서 연속된 B
left_b = 0
for c in color:
    if c == 'B':
        left_b += 1
    else:
        break

# 오른쪽에서 연속된 B
right_b = 0
for c in reversed(color):
    if c == 'B':
        right_b += 1
    else:
        break

# 4가지 경우 중 최소
answer = min(
    total_r - left_r,
    total_r - right_r,
    total_b - left_b,
    total_b - right_b
)

print(answer)