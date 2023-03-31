import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().split()
b = int(sys.stdin.readline())
lst = list(map(int, a))
print(lst.count(b))