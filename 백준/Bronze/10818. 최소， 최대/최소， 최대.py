import sys

num = int(sys.stdin.readline())
lst = sys.stdin.readline().split()
lst = list(map(int, lst))

print(min(lst), max(lst))