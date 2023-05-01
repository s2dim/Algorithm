import sys

t = int(sys.stdin.readline())

def recursion(word, l, r):
    if l >= r:
        cnt = 1
        recur = 1
    else:
        cnt = 1
        for i in range(0, len(word) // 2):
            if word[l+i] == word[r-i]:
                cnt += 1
                recur = 1

            else:
                recur = 0
                break
    
    return print(recur, cnt)

def isPallindrome(word):        
    return recursion(word, 0, len(word) - 1)


for i in range(t):
    a = input()
    isPallindrome(a)