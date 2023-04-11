a, b = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
prize = a[-b:]

print(min(prize))