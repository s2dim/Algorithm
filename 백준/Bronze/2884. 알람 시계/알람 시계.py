a, b = map(int, input().split())

if b < 45:
    m = b + 60 - 45
    if a == 0:
        h = 23
    else:
        h = a - 1
else:
    m = b - 45
    h = a

print(h, m)
