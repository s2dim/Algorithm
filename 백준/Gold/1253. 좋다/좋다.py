import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

ans = 0

max = num[-1]
cnt_lst = [0] * (n + 1)

for i in range(n):

    find = num[i]
    start_index = 0
    end_index = n - 1

    while start_index < end_index:
        start_index + end_index

        if num[start_index] + num[end_index] < find:
                start_index += 1
        elif num[start_index] + num[end_index] > find:
                end_index -= 1
        else:
            if start_index != i and end_index != i:
                ans += 1
                break
            elif start_index == i:
                start_index += 1
            elif end_index == i:
                 end_index -= 1

print(ans)