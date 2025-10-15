def solution(numbers):
    
    lst = [str(i) for i in numbers]
    lst.sort(key = lambda num : num * 3, reverse=True)

    answer = int(''.join(lst))
    return str(answer)