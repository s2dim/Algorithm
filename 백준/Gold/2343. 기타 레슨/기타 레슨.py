import sys

n, m = map(int, sys.stdin.readline().split())
video = list(map(int, sys.stdin.readline().split()))
total = sum(video)



def check(size):
    sum_ = 0
    cnt = 1
    for i in video:
        if i > size:
            return False

        if sum_ + i <= size:
            sum_ += i
        else:
            sum_ = i
            cnt += 1

        if cnt > m:
            return False # 사이즈가 작다

    return True


start = 0
end = total
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        end = mid - 1
    else:
        start = mid + 1

print(start)