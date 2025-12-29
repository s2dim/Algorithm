def solution(m, musicinfos):
    
    dic = {'C' : 'a', 'C#' : 'b', 'D' : 'c', 'D#' : 'd', 'E' : 'e', 'F' : 'f', 'F#' : 'g',
           'G' : 'h', 'G#' : 'i', 'A' : 'j', 'A#' : 'k', 'B' : 'l', 'B#' : 'm', 'E#' : 'o'}
    
    def change(word):
        memory = ''
        move = 0
        while move <= len(word)-1: # move가 마지막 인덱스보다 작아야 함
            if move == len(word) - 1:
                memory += dic.get(word[move])
                break
            elif word[move + 1] == '#':
                memory += dic.get(word[move:move+2])
                move += 2
            else:
                memory += dic.get(word[move])
                move += 1
        return memory
    
    m = change(m)
    m_len = len(m)

        
    lst = []
    for i in musicinfos:
        temp = i.split(',')
        new = []
        
        # 시간
        hour = int(temp[1][:2]) - int(temp[0][:2])
        minu = int(temp[1][3:]) - int(temp[0][3:])
        time = 60 * hour + minu
        
        # 음
        music = change(temp[3])
        
        new.append(time) # 재생 시간 0
        new.append(temp[2]) # 타이틀 1 
        new.append(music) # 음 2
        lst.append(new)
    
    max_ = 0
    answer = ''
    
    for new in lst:
        time, title, music = new
        if m_len > time:
            continue
        else:
            music_len = len(music) # 음악 길이
            if music_len > time: # 음악 길이가 재생 시간보다 길면
                play = music[:time] # 재생 시간 만큼만 자르기
            else:
                play = music * (time // music_len) + music[:time % music_len]

            
            idx = play.find(m)
            if idx != -1:
                if time > max_:
                    max_ = time
                    answer = title
                    
    if max_ == 0:
        return '(None)'
    else:
        return answer

    return 0
'''
1) 끝부분 + 처음 부분
2) 들은 그 곡이 아닐 수 있음

---
- 음악은 반드시 처음부터 재생
- 음악 길이보다 재생시간이 길면 반복 재생
- 
'''