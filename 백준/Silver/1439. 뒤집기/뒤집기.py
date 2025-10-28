
import sys

s = list(map(int, sys.stdin.readline().rstrip()))

cnt = [0, 0]
state = s[0]
cnt[state] += 1

for i in range(1, len(s)):
    if s[i] == state:
        continue
    else:
        state = s[i]
        cnt[state] += 1

print(min(cnt))