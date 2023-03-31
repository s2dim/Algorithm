import sys
n = int(sys.stdin.readline())
score = sys.stdin.readline().split()
score = list(map(int, score))

lst = []
max_score = max(score)
for i in score:
    new = i / max_score * 100
    lst.append(new)

print(sum(lst) / n)