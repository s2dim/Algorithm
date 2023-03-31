import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = sys.stdin.readline().split()
    word = [b[i] * int(a) for i in range(len(b))]
    text = ''.join(str(i) for i in word)
    print(text)