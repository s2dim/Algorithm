from itertools import product

def solution(word):
    word_lst = []
    lst = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        pro = list(product(lst, repeat=i))
        for j in pro:
            word_lst.append(''.join(j))
    word_lst.sort()

    text = [word[i] for i in range(len(word))]
    

    return word_lst.index(word)+1

# from collections import deque
# from itertools import product

# def solution(word):
#     words = []
#     for i in range(1, 6):
#         for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
#             words.append(''.join(list(c)))
    
#     words.sort()
#     print(words)
#     return words.index(word) + 1

'''
A
AA
AAA
AAAA
AAAAA


'''