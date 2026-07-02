def solution(record):
    lst = []
    members = {}
    answer = []
    
    for i in record:
        lst.append(i.split())
    
    for i in lst:
        state = i[0]
        user = i[1]
        if state != 'Leave': # leave가 아닐 때
            nickname = i[2]
            members[user] = nickname
    
    for i in lst:
        state = i[0]
        user = i[1]
        if state == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(members[user]))
        elif state == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(members[user]))
    return answer