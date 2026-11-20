def solution(today, terms, privacies):
    answer = []
    dic = {}
    
    # 약관 추가
    for i in terms:
        term, period = i.split()
        dic[term] = int(period)
    
    def calendar(date, term):
        year, month, day = map(int, date.split('.'))
        if month + dic[term] > 12:
            if (month + dic[term]) % 12 == 0:
                year += (month + dic[term]) // 12 - 1
                month = 12
            else:
                year += (month + dic[term]) // 12
                month = (month + dic[term]) % 12

        else:
            month = month + dic[term]
        return str(year) + str(month).zfill(2) + str(day).zfill(2)
    
    today = today.replace('.', '')
    
    for i in range(len(privacies)):
        date, term = privacies[i].split(' ')
        privacy = calendar(date, term)
        if privacy <= today:
            answer.append(i + 1)


    return answer

