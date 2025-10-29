import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    a = sys.stdin.readline().rstrip()
    arr.append(a)

block1 = ['WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW']

block2 = ['BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB']

min_ = int(1e9)
for i in range(0, n-7):
    for j in range(0, m-7):
        cnt1 = 0
        cnt2 = 0

        for x in range(8):
            for y in range(8):
                if arr[i+x][j+y] != block1[x][y]:
                    cnt1 += 1
                if arr[i+x][j+y] != block2[x][y]:
                    cnt2 += 1

        min_ = min(min_, cnt1, cnt2)

print(min_)