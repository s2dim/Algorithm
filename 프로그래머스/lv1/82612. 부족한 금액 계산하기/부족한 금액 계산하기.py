def solution(price, money, count):

    pay = [price * i for i in range(1, count+1)]
    answer = money - sum(pay)
    if answer < 0:
        answer = answer * (-1)
    else:
        answer = 0
            
    return answer

