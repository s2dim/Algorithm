from itertools import product
from bisect import bisect_left
def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    lst = []
    
    for i in range(1, 6):
        temp = list((product(words, repeat=i)))
        for j in temp:
            lst.append(''.join(j))
    
    lst.sort()
    answer = bisect_left(lst, word)
    return answer + 1