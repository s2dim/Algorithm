import sys
text = sys.stdin.readline().strip()

text = text.upper()

# 알파벳별로 각각 리스트에 저장
lst = [text[i] for i in range(len(text))]
a = list(set(lst))

# 각 글자가 몇 번 나오는지 계산
cnt = [lst.count(i) for i in a if i in lst]

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(a[cnt.index(max(cnt))])