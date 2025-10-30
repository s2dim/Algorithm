def solution(record):
    
    def message(ent, userid):
        if ent == 'Enter':
            text = f"{dic.get(userid)}님이 들어왔습니다."
        elif ent == 'Leave':
            text = f"{dic.get(userid)}님이 나갔습니다."
        return text
    
    dic = {}
    state = []
    
    for i in record:
        if i.startswith('Enter'):
            ent, userid, nick = i.split()
            state.append([ent, userid])
            dic[userid] = nick
        elif i.startswith('Leave'):
            ent, userid = i.split()
            state.append([ent, userid])
        elif i.startswith('Change'):
            ent, userid, nick = i.split()
            dic[userid] = nick
        
    answer = []
    for i in state:
        ent, userid = i
        answer.append(message(ent, userid))
    
    return answer

'''


'''