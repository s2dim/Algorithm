import sys
a = input()
lst = [int(a[i]) for i in range(len(a))]
lst.sort(reverse=True)
new_lst = [str(i) for i in lst]
text = ''.join(new_lst)

print(text)