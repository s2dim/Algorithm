def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()  # 1단계
    okay = ['-', '_', '.']
    
    temp = '' # 2단계
    before = ''
    for i in new_id: 
        if i.isdigit() or i in okay or i.islower():
            if i == '.' and before == '.': # 3단계
                continue
            temp += i
            before = i

    temp = temp.strip('.') # 4단계
    
    if not temp: # 5단계
        temp = 'a'
    
    if len(temp) >= 16: # 6단계
        temp = temp[:15]
        temp = temp.rstrip('.')
    
    if len(temp) <= 2: # 7단계
        last = temp[-1]
        while len(temp) < 3:
            temp += last
    return temp