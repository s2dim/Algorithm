import sys
a, b = sys.stdin.readline().split()

a = [(a[-i]) for i in range(1, len(a) + 1)]
b = [(b[-i]) for i in range(1, len(b) + 1)]

new_a = int(''.join(a))
new_b = int(''.join(b))

print(max(new_a, new_b))
