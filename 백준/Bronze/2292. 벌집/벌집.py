a = int(input())
min = 1
cnt = 0

while a > min:
    cnt += 1
    min = min + 6 * cnt

print(cnt + 1)