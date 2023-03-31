import sys
a = sys.stdin.readline()

word = [a[i] for i in range(len(a))]

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cnt = []
for i in lst:
    if i in word:
        cnt.append(word.index(i))
    else:
        cnt.append(-1)

print(*cnt)

