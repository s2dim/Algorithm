n = int(input())

a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

x_1 = max(a) - min(a)
y_1 = max(b) - min(b)

print(x_1 * y_1)