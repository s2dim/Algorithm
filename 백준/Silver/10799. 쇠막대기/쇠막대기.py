s = input()
n = len(s)

stack = []

stick = []
lazer = []

cnt = 0
for i in range(n):
    if s[i] == '(':
        stack.append(i)
    
    else:
        if s[i-1] == '(': # ()
            stack.pop()
            cnt += len(stack)
        else: # 나무가 끝나서 1조각 나옴
            stack.pop()
            cnt += 1


print(cnt)