def solution(name):
    # 각 글자마다 움직여야 하는 횟수
    
    def moving(word):
        cnt = min(ord(word) - 65, 91 - ord(word))
        return cnt
    
    alpha = [i for i in name]
    answer = 0
    for i in alpha:
        answer += moving(i)
        
    direct = len(name) - 1

    for i in range(len(name)):
        next = i + 1

        while next < len(name) and name[next] == 'A':
            next += 1

        direct = min(
            direct, i * 2 + len(name) - next, i + 2 * (len(name) - next))
                    
    return answer + direct


'''

91 90  89  88  87  86  85  84  83  82  81  80  79  78  77  76  75  74  73  72  71  70  69  68
A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X 65 66  67  68  69  70  71   72  73  74  75 76  77  78  79  80  81  82  83   84  85 86  87  88 

67  66
Y  Z
89 90
'''