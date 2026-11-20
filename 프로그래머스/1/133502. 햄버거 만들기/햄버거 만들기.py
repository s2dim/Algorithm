def solution(ingredient):
    stack = []
    answer = 0
    
    for i in ingredient:
        stack.append(i)
        if i == 1 and stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            answer += 1
    return answer