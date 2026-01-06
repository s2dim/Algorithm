import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
total = int(input())

start = min(total // n, min(lst))
end = max(lst)

def check(budget):
    sum_ = 0
    for i in lst:
        sum_ += min(i, budget) 
        if sum_ > total:
            return False # 예산 줄여야 됨
    return True 

while start <= end:
    mid = (start + end) // 2
    if check(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)