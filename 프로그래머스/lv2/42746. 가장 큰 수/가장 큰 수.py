def solution(numbers):
    
    lst = list(map(str, numbers))
#     lst.sort(reverse=True)
    lst.sort(key=lambda x : x * 3, reverse=True)
    
    if lst[0] == "0":
        answer = "0"
    else:
        answer = ''.join(lst)


    return answer