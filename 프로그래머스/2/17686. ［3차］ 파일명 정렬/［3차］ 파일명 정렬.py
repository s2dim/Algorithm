def solution(files):
    answer = []
    
    head = []
    number = []
    tail = []
    
    for f in files:
        print(f)
        for i in range(len(f)):
            if f[i].isdecimal():
                h = i
                head.append(f[:h])
                break
        
        n = -1
        for i in range(h, len(f)):
            if not f[i].isdecimal() or i-h > 5:
                n = i
                number.append(f[h:n])
                break
        if n == -1:
            number.append(f[h:])
            tail.append('')
            
        elif len(f) >= n:
            tail.append(f[n:])

    # print(head)
    # print(number)
    # print(tail)
    
    
    #############
    
    lst = []
    
    for i in range(len(head)):
        new = (head[i].lower(), int(number[i]), i)
        lst.append(new)
    
    lst = sorted(lst, key=lambda x:(x[0], x[1], x[2]))
    
    for i in lst:
        idx = i[2]
        answer.append(head[idx]+number[idx]+tail[idx])
    return answer

'''
파일명 -> 넘버 순 -> 들어온 순

1. 문자가 끝날 때까지 head
2. 다음 숫자가 끝날 때까지 number
3. 나머지 tail

head와 tail까지 포멧 맞춰서 정렬

'''