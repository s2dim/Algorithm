import copy

def solution(s):
    cnt = 0
    b = copy.deepcopy(s)
    
    for i in range(len(s)-1):
        cnt_ = 0
        a = copy.deepcopy(s)
        
        for i in range(len(s) // 2):
            
            if '{}' in a:
                a = a.replace('{}', '')
                cnt_ += 1
                
            elif '[]' in a:
                a = a.replace('[]', '')
                cnt_ += 1
                
            elif '()' in a:
                a = a.replace('()', '')
                cnt_ += 1
                
            if not a:
                cnt += 1
                break
                

        
        s = s[1:len(s)] + s[0]



        
    return cnt


'''
0 1 2 3 4 5
1 2 3 4 5 0
2 3 4 5 0 1

0 1 2
1 2 0

"}]()[{"
]()[{} - 1
()[{}] - 2
'''