text = input()
a = [text[i] for i in range(len(text))]
b = list(reversed(a))

if a == b:
    print(1)
else:
    print(0)
